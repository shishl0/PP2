from datetime import datetime

def current_datetime_no_microseconds():
    now = datetime.now().replace(microsecond=0)
    print("Current datetime without microseconds:", now)

if __name__ == "__main__":
    print("\n=== Datetime Without Microseconds ===")
    current_datetime_no_microseconds()