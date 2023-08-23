import requests
import subprocess
from datetime import datetime, timedelta
import time

# Global variables to store fetched prayer times and last played times
prayer_times_cache = []
last_played_times = {}

def fetch_prayer_times():
    global prayer_times_cache
    
    # Fetch prayer times only if the cache is empty or more than 5 times a day has passed
    if not prayer_times_cache or (datetime.now() - prayer_times_cache[-1]['fetch_time']).total_seconds() >= 86400 / 5:
        url = "http://mpt.i906.my/mpt.json?code=wlp-0&filter=1"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            prayer_times_cache = data['response']['times']
            prayer_times_cache[-1]['fetch_time'] = datetime.now()  # Record fetch time
        except requests.exceptions.RequestException as e:
            print("An error occurred while fetching prayer times:", e)

def play_azan(audio_file):
    try:
        subprocess.run(['mpg321', audio_file], check=True)
        last_played_times[audio_file] = datetime.now()  # Record last played time
    except subprocess.CalledProcessError:
        print("Error playing Azan audio:", audio_file)

def main():
    while True:
        fetch_prayer_times()

        if not prayer_times_cache:
            print("No prayer times data available.")
            time.sleep(7200)  # Wait for 2 hours
            continue

        azan_files = {
            "Fajr": "azan2.mp3",
            "Dhuhr": "azan.mp3",
            "Asr": "azan.mp3",
            "Maghrib": "azan.mp3",
            "Isha": "azan.mp3"
        }

        current_time = datetime.now()

        for time_entry in prayer_times_cache:
            prayer_time = datetime.fromtimestamp(time_entry['time'])
            prayer_name = datetime.strftime(prayer_time, "%H:%M")
            
            if prayer_name in azan_files and prayer_name not in last_played_times:
                time_difference = (prayer_time - current_time).total_seconds()
                if 0 <= time_difference <= 300:  # Within 5 minutes
                    print(f"It's time for {prayer_name} prayer!")
                    play_azan(azan_files[prayer_name])
        
        # Wait for 2 minutes before checking again
        time.sleep(120)

if __name__ == "__main__":
    main()
