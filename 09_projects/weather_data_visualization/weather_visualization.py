from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

path = Path("data/weather.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, header_column in enumerate(header_row):
#     print(index,header_column)

temps, dates = [],[]
for row in reader:
    formatted_date = datetime.strptime(row[1],'%Y-%m-%d')
    temps.append(row[10])
    dates.append(formatted_date)

fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.set_title("Temps")
ax.set_ylabel("Temperature", fontsize = 16, color="red")
ax.plot(dates, temps, color="blue")
plt.show()


