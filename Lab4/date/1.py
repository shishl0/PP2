from datetime import datetime, timedelta

def subtract_five_days():
    current_date = datetime.now()
    five_days_ago = current_date - timedelta(days=5)
    print("Current date:", current_date)
    print("Date 5 days ago:", five_days_ago)

if __name__ == "__main__":
    print("=== Subtract Five Days ===")
    subtract_five_days()