# Python3-Azan-Prayer-For-Raspberry-Pi
Fetch prayer times from e-solat and play azan.mp3


1. **Requirements:**
   - Ensure you have Python 3 installed on your system.
   - Download the `azan.py` script and the MP3 audio file.

2. **Running the Script:**
   - Place both `azan.py` and MP3 files in the same folder.
   - Open a terminal or command prompt.
   - Navigate to the folder where `azan.py` is located.
   - Run the script using the command: `python3 azan.py`
   - The script will check for prayer times every 60 or 120 seconds and play the Azan audio if it's time for prayer.

3. **Running on Boot (Optional):**
   - To have the script run automatically on every boot, follow these steps:
     - Open your terminal or command prompt.
     - Type `crontab -e` to edit the crontab file.
     - Add the following line to the crontab file:
       ```
       @reboot python3 /path/to/azan.py
       ```
     - Replace `/path/to/azan.py` with the actual path to your `azan.py` script.
     - Save and exit the editor.
     - The script will now run every time your system reboots, checking for prayer times and playing the Azan audio.

Note: Make sure to replace `/path/to/azan.py` with the correct path to your `azan.py` script. If you placed both files in the same folder, you can just use the script's filename (e.g., `/home/user/azan.py`).

Remember to adjust permissions as needed to ensure that the script can be executed and that the audio file is accessible.

P/S: Try azan2.py

73,

9M2PJU
