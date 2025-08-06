from datetime import datetime, timedelta

current_datetime = datetime.now()
print(f"Current Date and Time: {current_datetime}")
future_date = current_datetime+timedelta(days=10)
print(f"10 Days from Now: {future_date}")
formatted_date = future_date.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")