# Raspberry Pi Automated Prayer Times Retrieval and Azan Playback (Python 3)

This project is centered around effortlessly obtaining precise prayer times from e-solat and automatically playing the corresponding azan.mp3 files on a Raspberry Pi. To successfully establish and operate the project, adhere to the ensuing instructions:

## Prerequisites:

1. Verify the presence of Python 3 and MPG123 on your system.
2. Acquire the `fetch_prayer.py` and `read_prayer.py` scripts, along with the essential MP3 audio files.

## Executing the Script:

1. Position both `.py` files and the MP3 files within the same directory.
2. Launch a terminal or command prompt.
3. Navigate to the directory housing the `fetch_prayer.py` script.
4. Execute the script using this command: `python3 fetch_prayer.py`
   - This script will retrieve the most up-to-date prayer times.
5. Re-run the script by employing this command: `python3 read_prayer.py`
   - This script will establish crontab settings to automatically play the azan files at their designated times.

**Pro Tip**: For convenience, you can schedule the daily execution of `fetch_prayer.py` and `read_prayer.py` scripts using cron. This guarantees access to the latest e-solat prayer times. Remember to modify the username in `read_prayer.py` line 19 and region code in `fetch_prayer.py` line 23. Refer to https://mpt.i906.my/code.html for guidance.

73,

9M2PJU
