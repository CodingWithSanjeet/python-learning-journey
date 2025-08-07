# Weather Data Visualization

A Python application that reads weather data from CSV files and creates interactive temperature visualizations using matplotlib.

## Features

- **CSV Data Processing**: Read and parse weather data from CSV files
- **Time Series Visualization**: Plot temperature data over time
- **Date Formatting**: Automatic date parsing and formatting for x-axis
- **Interactive Plots**: Matplotlib-powered visualizations with zoom and pan capabilities

## Project Structure

```
weather_data_visualization/
├── weather_visualization.py    # Main visualization script
├── requirements.txt           # Python dependencies
├── data/                     # Data directory
│   └── weather.csv          # Sample weather data
└── README.md                # This file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Navigate to the project directory**
   ```bash
   cd 09_projects/weather_data_visualization
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install matplotlib
   ```

## Usage

### Quick Start

1. **Ensure data file exists**
   - Place your weather CSV file in the `data/` directory
   - Default filename: `weather.csv`

2. **Run the visualization**
   ```bash
   python weather_visualization.py
   ```

3. **View the plot**
   - A matplotlib window will open showing the temperature visualization
   - Use mouse to zoom, pan, and interact with the plot

### Data Format

The CSV file should contain weather data with the following structure:

| Column Index | Description | Example |
|--------------|-------------|---------|
| 0 | Station ID | "STATION123" |
| 1 | Date | "2023-01-01" |
| ... | Other columns | ... |
| 10 | Temperature | "25.5" |

**Required columns:**
- Column 1: Date in `YYYY-MM-DD` format
- Column 10: Temperature values (numeric)

### Customization

#### Using Different Data Files

To use a different CSV file, modify the path in `weather_visualization.py`:

```python
# Change this line
path = Path("data/weather.csv")

# To your file
path = Path("data/your_weather_data.csv")
```

#### Customizing the Plot

You can modify various aspects of the visualization:

```python
# Chart title
ax.set_title("Your Custom Title")

# Y-axis label and color
ax.set_ylabel("Temperature (°C)", fontsize=16, color="red")

# Line color and style
ax.plot(dates, temps, color="blue", linewidth=2, linestyle="-")

# Figure size
fig, ax = plt.subplots(figsize=(12, 6))
```

#### Adding More Data Series

To plot additional temperature data (e.g., min/max temperatures):

```python
temps_max, temps_min = [], []
for row in reader:
    formatted_date = datetime.strptime(row[1], '%Y-%m-%d')
    temps.append(row[10])      # Current temperature
    temps_max.append(row[11])  # Maximum temperature
    temps_min.append(row[9])   # Minimum temperature
    dates.append(formatted_date)

# Plot multiple lines
ax.plot(dates, temps, color="blue", label="Temperature")
ax.plot(dates, temps_max, color="red", label="Max Temperature")
ax.plot(dates, temps_min, color="green", label="Min Temperature")
ax.legend()
```

## Example Output

The script generates a line plot showing:
- X-axis: Dates (automatically formatted)
- Y-axis: Temperature values
- Blue line connecting temperature data points
- Interactive matplotlib interface for exploration

## Troubleshooting

### Common Issues

1. **File not found error**
   ```
   FileNotFoundError: [Errno 2] No such file or directory: 'data/weather.csv'
   ```
   - **Solution**: Ensure `weather.csv` exists in the `data/` directory
   - Check file name spelling and location

2. **Date parsing errors**
   ```
   ValueError: time data 'invalid_date' does not match format '%Y-%m-%d'
   ```
   - **Solution**: Ensure dates in CSV are in `YYYY-MM-DD` format
   - Check for empty or malformed date entries

3. **Import errors**
   ```
   ModuleNotFoundError: No module named 'matplotlib'
   ```
   - **Solution**: Install required packages using `pip install -r requirements.txt`

4. **Empty plot or no data**
   - Check if CSV file contains data
   - Verify column indices (date=1, temperature=10) match your data
   - Ensure temperature values are numeric

### Data Debugging

To debug your CSV data, uncomment the header inspection code:

```python
# Uncomment these lines to see column headers and indices
for index, header_column in enumerate(header_row):
    print(index, header_column)
```

This will show you the column structure of your CSV file.

## Dependencies

- **matplotlib**: Plotting and visualization library
  - Version: 3.7.0 or higher
  - Used for: Creating line plots, date formatting, interactive displays

- **pathlib**: File path handling (built-in to Python 3.4+)
  - Used for: Cross-platform file path operations

- **datetime**: Date and time handling (built-in)
  - Used for: Parsing and formatting date strings

- **csv**: CSV file processing (built-in)
  - Used for: Reading and parsing CSV data

## Sample Data

The included `weather.csv` contains sample weather data with temperature readings over time. You can replace this with your own weather data following the same format.

## Future Enhancements

Potential improvements for this project:

- Add support for multiple weather stations
- Include additional weather parameters (humidity, pressure, etc.)
- Add data filtering and date range selection
- Implement statistical analysis (averages, trends)
- Export plots to image files
- Add command-line arguments for customization
- Support for different date formats
- Interactive web-based visualization

## License

This project is for educational purposes. Feel free to modify and extend for your learning needs.

---

**Note**: This visualization tool is designed for learning data analysis and plotting with Python. For production weather applications, consider additional data validation and error handling.