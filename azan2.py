import requests
import subprocess
from datetime import datetime
import time

# Global variables to store fetched prayer times and last played times
prayer_times_cache = []
last_played_times = {}

def fetch_prayer_times(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        prayer_times = data['response']['times']
        return prayer_times
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching prayer times:", e)
        return []

def play_azan(audio_file):
    try:
        subprocess.run(['mpg123', audio_file], check=True)
        last_played_times[audio_file] = datetime.now()  # Record last played time
    except subprocess.CalledProcessError:
        print("Error playing Azan audio:", audio_file)

def main():
    fetch_url = "https://mpt.i906.my/mpt.json?code=wlp-0&filter=1"

    while True:
        current_time = datetime.now()
        
        # Fetch prayer times now
        print("Fetching current prayer times...")
        prayer_times = fetch_prayer_times(fetch_url)
        if prayer_times:
            prayer_times_cache = prayer_times

        azan_files = {
            0: "azan2.mp3",  # Fajr
            1: "azan.mp3",   # Dhuhr, Asr, Maghrib, Isha
        }

        for idx, prayer_time in enumerate(prayer_times_cache):
            if idx == 0:  # Fajr
                azan_file = azan_files[0]
            elif idx == 1:  # Sunrise, skip
                continue
            else:  # Dhuhr, Asr, Maghrib, Isha
                azan_file = azan_files[1]
            
            prayer_datetime = datetime.fromtimestamp(prayer_time)
            time_difference = (prayer_datetime - current_time).total_seconds()
            
            if 0 <= time_difference <= 300:  # Within 5 minutes
                print(f"It's time for {idx} prayer!")
                play_azan(azan_file)

        time.sleep(3600)  # Wait for 1 hour before checking again

if __name__ == "__main__":
    main()
