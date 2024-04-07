import datetime
import time


def task_scheduler(task, date_time):
    """Schedule a task with a specific date and time."""
    scheduled_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
    current_time = datetime.datetime.now()

    if scheduled_time > current_time:
        time_difference = scheduled_time - current_time
        seconds_until_task = time_difference.total_seconds()
        time.sleep(seconds_until_task)
        return f"Reminder: It's time to '{task}' now!"
    else:
        print(f"The provided time for '{task}' has already passed.")
