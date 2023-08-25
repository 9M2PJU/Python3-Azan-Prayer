# Automated Azan Prayer Times Retrieval and Playback for Raspberry Pi (Python 3)

This project focuses on fetching accurate prayer times from e-solat and playing the azan.mp3 files automatically on a Raspberry Pi. To set up and run the project, follow the steps below:

## Requirements:

1. Make sure you have Python 3 and MPG123 installed on your system.
2. Download the `fetch_prayer.py` and `read_prayer.py` scripts along with the necessary MP3 audio files.

## Running the Script:

1. Place both the `.py` files and the MP3 files in the same directory.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the `fetch_prayer.py` script.
4. Execute the script using the following command: `python3 fetch_prayer.py`
   - This script will retrieve the latest prayer times.
5. Run the script again by using the command: `python3 read_prayer.py`
   - This script will set up crontab values to play the azan files at their designated times.

**Note**: For convenience, you can schedule the `fetch_prayer.py` and `read_prayer.py` scripts to run daily using cron. This ensures that you always have the most up-to-date prayer times from e-solat.

73,

9M2PJU
