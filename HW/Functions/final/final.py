import threading
import time
import platform
import random
from plyer import notification

class CustomNotifier:
    def __init__(self):
        self.platform = platform.system()

    def show_notification_at_specific_time(self, hour, minute, second, icon_path=None):
        def display_notification():
            if self.platform in ['Windows', 'Linux']:
                current_time = time.localtime()
                scheduled_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, hour, minute, second, -1, -1, -1))

                if time.mktime(scheduled_time) <= time.mktime(current_time):
                    scheduled_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday + 1, hour, minute, second, -1, -1, -1))

                time_until_notification = time.mktime(scheduled_time) - time.mktime(current_time)

                time.sleep(time_until_notification)
                notification.notify(title="A message for you ;))", message="Hey, you're cute", timeout=5, app_icon=icon_path)

        threading.Thread(target=display_notification).start()

    def schedule_random_notification(self):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        self.show_notification_at_specific_time(hour, minute, second)

    def on_notification_click(self):
        print("Notification clicked!")
        # Schedule the same notification to display again after a random interval
        random_interval = random.randint(10, 60)  # Random interval between 10 and 60 seconds
        threading.Timer(random_interval, self.schedule_random_notification).start()

# Example usage:
notifier = CustomNotifier()
notifier.schedule_random_notification()
