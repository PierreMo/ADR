from datetime import datetime
import time

def wait_until_time(new_time_str):
    # adjusting to format
    dt = datetime.strptime(new_time_str, "%Y-%m-%d %H:%M:%S")
    # computing time to wait
    current_time = datetime.now()
    time_remaining = dt - current_time

    # Wait until the target time
    if time_remaining.total_seconds() > 0:
        time.sleep(time_remaining.total_seconds())
    else:
        print("The target time is in the past.")