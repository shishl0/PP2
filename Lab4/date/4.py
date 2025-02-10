from datetime import datetime, timedelta

def date_difference_in_seconds():
    date1 = datetime.now()
    date2 = date1 - timedelta(days=1, hours=2, minutes=30)
    diff_seconds = abs((date1 - date2).total_seconds())
    print("Difference in seconds:", diff_seconds)

if __name__ == "__main__":
    print("\n=== Date Difference in Seconds ===")
    date_difference_in_seconds()