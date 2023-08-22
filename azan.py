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

def play_azan():
    subprocess.run(['mpg321', 'azan.mp3'])  # Replace 'azan.mp3' with the actual path to your Azan audio file

def main():
    prayer_times = fetch_prayer_times()

    if not prayer_times:
        print("No prayer times data available.")
        return

    prayers = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]

    while True:
        current_time = datetime.now()

        for idx, time_epoch in enumerate(prayer_times):
            prayer_time = datetime.fromtimestamp(time_epoch)

            if current_time.time() <= prayer_time.time() <= (current_time + timedelta(minutes=5)).time():
                prayer_name = prayers[idx]
                print(f"It's time for {prayer_name} prayer!")
                play_azan()
                break

        # Wait for one minute before checking again
        time.sleep(60)

if __name__ == "__main__":
    main()
