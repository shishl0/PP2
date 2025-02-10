from datetime import datetime, timedelta

def print_surrounding_dates():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    date_format = "%Y-%m-%d"
    print("Yesterday:", yesterday.strftime(date_format))
    print("Today:    ", today.strftime(date_format))
    print("Tomorrow: ", tomorrow.strftime(date_format))

if __name__ == "__main__":
    print("\n=== Yesterday, Today, Tomorrow ===")
    print_surrounding_dates()