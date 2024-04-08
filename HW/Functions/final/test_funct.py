def test_schedule_notification():
    # Test scheduling a notification
    notifier = CustomNotifier()
    notifier.schedule_random_notification()
    print("Notification scheduled successfully.")

def test_notification_click():
    # Test handling notification click
    notifier = CustomNotifier()

    def simulate_notification_click():
        # Simulate a notification click
        print("Simulating notification click...")
        notifier.on_notification_click()
        print("Notification click handled successfully.")

    # Start a separate thread to simulate notification click after 5 seconds
    threading.Timer(5, simulate_notification_click).start()

# Run the test functions
test_schedule_notification()
test_notification_click()
