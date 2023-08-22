import requests
import subprocess
from datetime import datetime, timedelta
import time

def fetch_prayer_times():
    url = "http://mpt.i906.my/mpt.json?code=wlp-0&filter=1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status code indicates an error
        data = response.json()
        return data['response']['times']
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching prayer times:", e)
        return []

def play_azan(audio_file):
    subprocess.run(['mpg321', audio_file])

def main():
    prayer_times = fetch_prayer_times()

    if not prayer_times:
        print("No prayer times data available.")
        return

    azan_files = {
        "Fajr": "azan2.mp3",
        "Dhuhr": "azan.mp3",
        "Asr": "azan.mp3",
        "Maghrib": "azan.mp3",
        "Isha": "azan.mp3"
    }

    while True:
        current_time = datetime.now()

        for time_epoch in prayer_times:
            prayer_time = datetime.fromtimestamp(time_epoch)

            for prayer_name, audio_file in azan_files.items():
                if current_time.time() <= prayer_time.time() <= (current_time + timedelta(minutes=5)).time():
                    print(f"It's time for {prayer_name} prayer!")
                    play_azan(audio_file)
                    break

        # Wait for one minute before checking again
        time.sleep(60)

if __name__ == "__main__":
    main()
