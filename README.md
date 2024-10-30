
## 🌐 Socials:
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white)](https://facebook.com/https://www.facebook.com/faizul.9m2pju) [![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?logo=TikTok&logoColor=white)](https://tiktok.com/@9m2pju) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://youtube.com/@http://www.youtube.com/@9m2pju) 

# 💻 Tech Stack:
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white) ![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515) ![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=9M2PJU&theme=dark&hide_border=false&include_all_commits=false&count_private=false)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=9M2PJU&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=9M2PJU&theme=dark&hide_border=false&include_all_commits=false&count_private=false&layout=compact)

## 🏆 GitHub Trophies
![](https://github-profile-trophy.vercel.app/?username=9M2PJU&theme=radical&no-frame=false&no-bg=true&margin-w=4)

---
[![](https://visitcount.itsvg.in/api?id=9M2PJU&icon=0&color=0)](https://visitcount.itsvg.in)

  ## 💰 You can help me by Donating
  [![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/9m2pju) 

  
<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->

# Automated Prayer Times Retrieval and Azan Playback (Python 3)

Demo video

https://youtube.com/shorts/0Jf2ifZXT9g?si=_En0I6R7lsk2ajxM


This project is centered around effortlessly obtaining precise prayer times from https://mpt.i906.my/index.html and automatically playing the corresponding azan.mp3 files. To successfully establish and operate the project, adhere to the ensuing instructions:

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
6. And lastly, edit your crontab by using `crontab -e` and add `0 5 * * * /usr/bin/python3 /home/dietpi/azan/fetch_prayer.py` and `1 5 * * * /usr/bin/python3 /home/dietpi/azan/read_prayer.py` so it will fetch and update daily prayer times.   


**Pro Tip**: For convenience, you can schedule the daily execution of `fetch_prayer.py` and `read_prayer.py` scripts using cron. This guarantees access to the latest e-solat prayer times. Remember to modify the username in `read_prayer.py` line 19 and region code in `fetch_prayer.py` line 23. Refer to https://mpt.i906.my/code.html for guidance.


