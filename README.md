# DataFit Perfectly-Matching Ideal Functions with Real-Data 
A Python project for mapping ideal and test data with precise visualizations. 🚀📊 Ideal for data fitting, analysis, and visualization. Built with 💻 Python, 📉 Plotly, and 📁 CSV data handling!
Here's a **README** file content template based on your project setup and code structure. This README describes each component, its purpose, dependencies, and how to use it.

---
https://github.com/user-attachments/assets/4f15db29-4156-4094-9421-932e14192e49

![image](https://github.com/user-attachments/assets/af88fb85-2536-407d-bd73-1ab8ee2048c1)
![image](https://github.com/user-attachments/assets/55fb19e1-eea4-4692-b6df-7d7e5dd0aeb0)


## Project Structure 📁

- **data** folder: Contains the input data files used in the project.
  - `ideal.csv` - Contains ideal functions data.
  - `train.csv` - Contains training data.
  - `test.csv` - Contains test data.
- **main.py** - Core script for processing data, finding best-fit functions, and visualizing results.
- **test_main.py** - Contains unit tests for the main functionalities of the project.
- **plot.html** - Generated interactive plot file.
- **data.db** - SQLite database file where processed data is saved.

## Libraries and Modules Used 🛠️

- **Pandas** - For data handling and manipulation.
- **NumPy** - For mathematical operations and calculations.
- **SQLAlchemy** - For creating and managing SQLite database connections.
- **Bokeh** - For interactive data visualization.
- **Unittest** - For testing the main functionalities of the project.

## Setup and Installation 📝

1. Clone this repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use .venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Data Files 📄

- **train.csv** - Training data used to determine the best-fitting functions.
- **ideal.csv** - Contains ideal functions that will be compared against the training data.
- **test.csv** - Test data mapped to the best-fit functions to evaluate deviation.

Ensure the data files are located in the **data** folder in the same directory as the scripts.

## Usage 🚀

### Running the Main Script

The main script (`main.py`) processes data, finds the best-fit functions, maps test data, and visualizes the results.

```bash
python main.py
```

### Plotting Results

After running `main.py`, the plot will be saved as `plot.html` and automatically opened in the default web browser. This interactive plot includes:
- **Training Data** - Plotted with distinct colors.
- **Ideal Functions** - Displaying only the best-fitting functions.
- **Test Data** - Displayed as scatter points to show mapping.

### Testing 🧪

Run unit tests to verify that the core functionalities work as expected:

```bash
python -m unittest test_main.py
```

## Code Overview 🧩

### `main.py`

- **IdealFunctionFitter Class** - Core logic for processing data, finding best-fit functions, and mapping test data.
  - `find_best_fit()` - Identifies the best ideal functions using least squares.
  - `map_test_data()` - Maps test data points to the best-fit functions and calculates deviations.

- **plot_data() function** - Uses Bokeh to create an interactive plot, visualizing training data, ideal functions, and test data points.

### `test_main.py`

Contains unit tests to verify functionality:
- **test_find_best_fit()** - Tests the best-fit function identification.
- **test_map_test_data()** - Checks that test data is mapped correctly.

## Results and Interpretation 🧾

The best-fit ideal functions are identified and visualized alongside training and test data. The output HTML plot provides an interactive exploration of data points and their corresponding ideal functions.

## License 📜

This project is licensed under the MIT License.
