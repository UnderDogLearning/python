""" Alarm Clock
----------------------------------------
"""
import datetime
import os
import time
import random
import webbrowser
"""// If video URL file does not exist, create one"""
if not os.path.isfile("youtube_alarm_videos.txt"):
    print('Creating "youtube_alarm_videos.txt"...')
    with open("youtube_alarm_videos.txt", "w") as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=anM6uIZvx74")
def check_alarm_input(alarm_time):
    """Checks to see if the user has entered in a valid alarm time"""
    if len(alarm_time) == 1:
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2: 
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3: 
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0 and alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False
"""// Get user input for the alarm time"""
print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
while True:
    alarm_input = input(">> ")
    print(alarm_input)
    try:
        alarm_time = [int(n) for n in alarm_input.split(":")]
        print(alarm_time)
        if check_alarm_input(alarm_time):
            print(alarm_time)
            break
        else:
            raise ValueError
    except ValueError:
        print("ERROR: Enter time in HH:MM or HH:MM:SS format")
"""// Convert the alarm time from [H:M] or [H:M:S] to seconds"""
seconds_hms = [3600, 60, 1] 
print(seconds_hms)
print(alarm_time)
print(len(alarm_time))
alarm_seconds = sum([a*b for a,b in zip(seconds_hms, alarm_time)])
print(f"Alarm set to {alarm_seconds}")
"""// Get the current time of day in seconds"""
now = datetime.datetime.now()
print(f"Current time is {now}")
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
print(f"Curren time in Sec {current_time_seconds}")
"""// Calculate the number of seconds until alarm goes off"""
time_diff_seconds = alarm_seconds - current_time_seconds
print(f"Time Difference is {time_diff_seconds}")
"""// If time difference is negative, set alarm for next day"""
if time_diff_seconds < 0:
    time_diff_seconds += 86400 
"""// Display the amount of time until the alarm goes off"""
print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))
"""// Sleep until the alarm goes off"""
time.sleep(time_diff_seconds)
"""// Time for the alarm to go off"""
print("Wake Up!")
webbrowser.open("https://www.youtube.com/watch?v=anM6uIZvx74")
