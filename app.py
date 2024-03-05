import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLineEdit, QPushButton, QLabel, QFileDialog

class DataAnalysisTool(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Analysis Tool")
        self.setGeometry(100, 100, 400, 250)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create a combo box for selecting the chart type
        self.chart_combobox = QComboBox()
        self.chart_combobox.addItems(["Scatter Plot", "Bar Chart", "Histogram"])
        layout.addWidget(self.chart_combobox)

        # Create input fields for column names
        self.x_input = QLineEdit()
        self.x_input.setPlaceholderText("X-Axis Column Name")
        layout.addWidget(self.x_input)

        self.y_input = QLineEdit()
        self.y_input.setPlaceholderText("Y-Axis Column Name")
        layout.addWidget(self.y_input)

        # Create a button to trigger data analysis
        analyze_button = QPushButton("Analyze Data")
        analyze_button.clicked.connect(self.analyze_data)
        layout.addWidget(analyze_button)

        central_widget.setLayout(layout)

    def load_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a data file")
        if file_path.endswith('.json'):
            data = pd.read_json(file_path)
        elif file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported data format. Please provide JSON or Excel data.")
        return data

    def analyze_data(self):
        data = self.load_data()
        selected_chart = self.chart_combobox.currentText()
        x_column = self.x_input.text().strip().capitalize()
        y_column = self.y_input.text().strip().capitalize()

        # Clear any previous chart and labels
        plt.clf()
        
        if selected_chart == "Scatter Plot" and x_column and y_column:
            data.plot(kind='scatter', x=x_column, y=y_column)
            plt.title("Scatter Plot")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
        elif selected_chart == "Bar Chart" and x_column:
            data[x_column].value_counts().plot(kind='bar')
            plt.title("Bar Chart")
            plt.xlabel(x_column)
            plt.ylabel("Count")
        elif selected_chart == "Histogram" and x_column:
            data[x_column].plot(kind='hist', bins=10)
            plt.title("Histogram")
            plt.xlabel(x_column)

        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataAnalysisTool()
    window.show()
    sys.exit(app.exec_())
