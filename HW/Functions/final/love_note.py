import threading
import time
import platform
import random

class CustomNotifier:
    def __init__(self):
        self.platform = platform.system()
        if self.platform in ['Windows', 'Linux']:
            from plyer import notification as notifier
        # Add support for other platforms here

    def show_notification_at_random_time(self, icon_path=None, callback=None, actions=None):
        """
        Display a custom desktop notification at a random time during the day.

        Args:
            icon_path (str, optional): Path to the icon image file to display in the notification. Defaults to None.
            callback (callable, optional): A function to be called when the notification is clicked. Defaults to None.
            actions (list of tuples, optional): Actions to be included in the notification, each tuple should be (action_name, callback_function). Defaults to None.
        """
        def display_notification():
            if self.platform in ['Windows', 'Linux']:
                while True:
                    # Generate a random time between 9:00 AM and 5:00 PM
                    random_hour = random.randint(9, 16)
                    random_minute = random.randint(0, 59)
                    random_second = random.randint(0, 59)
                    scheduled_time = time.struct_time((time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, random_hour, random_minute, random_second, -1, -1, -1))
                    current_time = time.localtime()

                    # If the generated time is earlier than the current time, adjust it to the next day
                    if scheduled_time < current_time:
                        scheduled_time = time.struct_time((time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday + 1, random_hour, random_minute, random_second, -1, -1, -1))

                    # Calculate the time until the notification should be shown
                    time_until_notification = time.mktime(scheduled_time) - time.mktime(current_time)

                    # Check if the time until notification is valid (greater than 0)
                    if time_until_notification > 0:
                        break

                # Sleep until it's time to show the notification
                time.sleep(time_until_notification)

                # Show the notification
                self.notification_id = notifier.notify(title="A message for you ;))", message="Hey, you're cute", timeout=5, app_icon=icon_path, callback=self.on_notification_click, actions=actions)

        if callback or actions:
            threading.Thread(target=display_notification).start()
        else:
            display_notification()

    def on_notification_click(self):
        print("Notification clicked!")

    # Example callback function for action 1
    def action1(self):
        print("Action 1 performed.")
        if self.platform in ['Windows', 'Linux']:
            notifier.dismiss(self.notification_id)  # Dismiss the current notification
            # Schedule another notification to display randomly during the day
            threading.Thread(target=self.show_notification_at_random_time).start()
            # Show a new notification with a different message
            notifier.notify(title="A message for you ;))", message="You are amazing!", timeout=5, app_icon=r"C:\Users\alext\Downloads\notification icon")

# Example usage:
notifier = CustomNotifier()
actions = [("Close", notifier.action1)]
notifier.show_notification_at_random_time(actions=actions)
