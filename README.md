
# Data Analysis Tool

This Python application provides a simple graphical user interface for analyzing data stored in either JSON or Excel format. It allows users to generate various types of charts such as scatter plots, bar charts, and histograms to visualize their data.

## Requirements
- Python 3.x
- PyQt5
- pandas
- matplotlib

## Usage
1. Clone or download the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application by executing `python data_analysis_tool.py`.

## Data Format
The data should be provided in JSON or Excel format. For JSON format, the data should be structured as follows:

```json
[
    {
        "Name": "John",
        "Age": 22,
        "Gender": "Male",
        "Grade": "A"
    },
    {
        "Name": "Alice",
        "Age": 21,
        "Gender": "Female",
        "Grade": "B"
    },
    ...
]
```

## How to Use
1. Launch the application.
2. Click on the "Analyze Data" button.
3. Select the data file (JSON or Excel) using the file dialog that appears.
4. Choose the type of chart you want to generate from the dropdown menu (Scatter Plot, Bar Chart, or Histogram).
5. Enter the column names for the X-Axis and Y-Axis (for Scatter Plot) or just the X-Axis (for Bar Chart and Histogram).
6. Click on "Analyze Data" button to generate the selected chart.

## Features
- Supports both JSON and Excel data formats.
- Allows selection of different types of charts.
- Provides interactive visualization of data.

## Example
Here's an example usage of the tool:

```python
python data_analysis_tool.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
