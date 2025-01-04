pip install pandas numpy sqlalchemy bokeh
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool

class IdealFunctionFitter:
    """
    This class is used to process training data and find the best fit from ideal functions.
    """
    def __init__(self, training_data, ideal_data):
        self.training_data = training_data
        self.ideal_data = ideal_data

    def find_best_fit(self, num_best_fits=4):
        """
        Find the best ideal functions for the training data using the least squares.
        :return: A list of the names of the best fit ideal functions.
        """
        errors = []
        for col in self.ideal_data.columns[1:]:
            for y_col in self.training_data.columns[1:]:
                error = np.sum((self.training_data[y_col] - self.ideal_data[col]) ** 2)
                errors.append((col, error))

        best_fits = sorted(errors, key=lambda x: x[1])[:num_best_fits]
        return [fit[0] for fit in best_fits]

    def map_test_data(self, test_data, best_fit_funcs):
        """
        Map test data to the best-fit ideal functions and calculate deviation.
        :param test_data: DataFrame containing test data.
        :param best_fit_funcs: List of best-fit ideal function names.
        :return: List of mapped test data with deviations.
        """
        results = []
        for index, row in test_data.iterrows():
            x_val = row['x']  # Get x value from test data
            y_val = row['y']  # Get y value from test data
            for func in best_fit_funcs:
                try:
                    ideal_y = self.ideal_data.loc[self.ideal_data['x'] == x_val, func].values[0]
                    deviation = np.abs(y_val - ideal_y)  # Calculate deviation
                    if deviation <= np.sqrt(2):
                        results.append((x_val, y_val, func, deviation))
                except IndexError:
                    continue
        return results

# Load CSV files for training, ideal functions, and test data
train1 = pd.read_csv('C:/Users/Ultimate Computers/Documents/train.csv')
ideal_funcs = pd.read_csv('C:/Users/Ultimate Computers/Documents/ideal.csv')
test_data = pd.read_csv('C:/Users/Ultimate Computers/Documents//test.csv')

# Set up SQLite database
engine = create_engine('sqlite:///data.db')

# Save training data to SQLite table
train_data_combined = pd.concat([train1], axis=1)  # Combine any additional training datasets if necessary
train_data_combined.to_sql('train_data', con=engine, index=False, if_exists='replace')
ideal_funcs.to_sql('ideal_functions', con=engine, index=False, if_exists='replace')

# Initialize the fitter and find the best fits
fitter = IdealFunctionFitter(train1, ideal_funcs)
best_fit_funcs = fitter.find_best_fit()

# Visualization function to plot training data, ideal functions, and test data
def plot_data(train_data, test_data, ideal_data, best_fit_funcs):
    p = figure(title="Data Visualization", tools="pan,wheel_zoom,box_zoom,reset,save")

    # Hover tool to show data points
    hover = HoverTool(tooltips=[("X", "$x"), ("Y", "$y")])
    p.add_tools(hover)

    # Plot all training functions with larger line width and contrast colors
    training_colors = ["blue", "green", "purple", "cyan"]
    for i, y_col in enumerate(train_data.columns[1:], start=0):
        p.line(train_data['x'], train_data[y_col], legend_label=f"Training {y_col}",
               line_width=2, color=training_colors[i % len(training_colors)], alpha=0.8)

    # Plot only the best fits
    for fit in best_fit_funcs:
        p.line(ideal_data['x'], ideal_data[fit], legend_label=f"Best Fit: {fit}",
               line_width=3, color="orange")

    # Plot limited ideal functions (show only the top 4 best fits)
    ideal_to_show = best_fit_funcs[:4]  # Show only top 4 best fits
    for col in ideal_data.columns[1:]:
        if col in ideal_to_show:
            p.line(ideal_data['x'], ideal_data[col], legend_label=f"Ideal {col}",
                   line_width=1, color="lightgray", line_dash="dotted", alpha=0.5)

    # Plot test data as red scatter points with labels
    p.scatter(test_data['x'], test_data['y'], size=10, color="red", legend_label="Test Data")

    # Set axis labels
    p.xaxis.axis_label = "X-axis"
    p.yaxis.axis_label = "Y-axis"

    # Set font size and increase contrast
    p.xaxis.axis_label_text_font_size = "14pt"
    p.yaxis.axis_label_text_font_size = "14pt"
    p.title.text_font_size = "16pt"

    # Set dynamic axis limits based on data ranges
    p.x_range.start = train_data['x'].min() - 1
    p.x_range.end = train_data['x'].max() + 1
    p.y_range.start = min(train_data.iloc[:, 1:].min().min(), test_data['y'].min()) - 10
    p.y_range.end = max(train_data.iloc[:, 1:].max().max(), test_data['y'].max()) + 10

    output_file("plot.html")  # Output the plot to an HTML file
    show(p)  # Display the plot

# Call the function to plot the data
plot_data(train1, test_data, ideal_funcs, best_fit_funcs)

# Map test data to the best fit functions and display the results
mapped_data = fitter.map_test_data(test_data, best_fit_funcs)

if __name__ == '__main__':
    print(f"Mapped Data: {mapped_data}")
