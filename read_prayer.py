import re
from crontab import CronTab

def read_prayer_times(file_path):
    prayer_times = []

    with open(file_path, "r") as file:
        for line in file:
            match = re.match(r"Prayer (\d+): \d{4}-\d{2}-\d{2} (\d{2}:\d{2}):\d{2}", line)
            if match:
                prayer_index = int(match.group(1))
                if prayer_index != 1:  # Exclude Prayer 1
                    prayer_time_str = match.group(2)
                    prayer_times.append((prayer_index, prayer_time_str))

    return prayer_times

def add_cron_jobs(prayer_times):
    cron = CronTab(user='dietpi')

    # Remove existing prayer time jobs
    cron.remove_all(comment="Prayer Time")

    for prayer_index, prayer_time_str in prayer_times:
        prayer_hour, prayer_minute = map(int, prayer_time_str.split(':'))
        if prayer_index == 0:
            audio_file = "/home/dietpi/azan2.mp3"
        else:
            audio_file = "/home/dietpi/azan.mp3"
        command = f"mpg123 {audio_file}"
        job = cron.new(command=command, comment="Prayer Time")
        job.setall(prayer_minute, prayer_hour, '*', '*', '*')

    cron.write()

def main():
    file_path = "prayer.txt"  # Path to prayer.txt
    prayer_times = read_prayer_times(file_path)
    add_cron_jobs(prayer_times)

if __name__ == "__main__":
    main()
