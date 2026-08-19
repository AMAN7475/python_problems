'''Sales & Profit Data Visualization Tool

Businesses often generate large amounts of sales and profit data, but raw numerical data can be difficult to understand and analyze effectively. Users need a simple way to transform this data into meaningful visual representations so that they can identify trends, distributions, comparisons, and relationships between different variables.

The objective of this project is to develop an interactive data visualization application using Python, Pandas, Matplotlib, and Gradio. The application takes monthly sales and profit data (January to June) as input and allows users to select the type of visualization they want to generate based on their analysis requirements.

The application supports multiple visualization techniques, including:

Line Plot - to analyze sales/profit trends over the months.
Bar Graph - to compare sales and profit across different months.
Histogram - to understand the distribution of numerical data.
Box Plot  - to analyze the spread, median, and potential outliers in the data.
Pie Chart - to visualize the proportional contribution of different categories/months.
Scatter Plot - to identify relationships or correlations between sales and profit.

The project provides an easy-to-use Gradio interface, allowing users to interact with the data and generate visualizations without directly writing Python or Matplotlib code.

Technologies Used
Python - Core programming language
Pandas - Data manipulation and analysis
Matplotlib - Data visualization
Gradio - Interactive web-based user interface'''

# ====================================================================
# Solution
# ====================================================================

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ['Jan', 'Feb', 'March', 'April', 'May', 'June'],
    "Sales": [10000, 12000, 15000, 13000, 17000, 16000],
    "Profit": [2000, 3000, 4000, 2500, 3500, 3000]
}

df = pd.DataFrame(data)


def greeting(type_graph):
    fig = plt.figure(figsize=(8, 4))

    if type_graph == 'boxplot':
        plt.boxplot(
            df['Profit'],
            orientation='vertical',
            patch_artist=True,
            boxprops=dict(facecolor='lightgreen')
        )
        plt.title('Profit Box Plot')
        plt.xlabel('Profit')
        plt.tight_layout()

    elif type_graph == 'lineplot':
        plt.plot(
            df['Month'],
            df['Sales'],
            color='blue',
            marker='o',
            linestyle='-',
            label='Sales'
        )
        plt.title('Sales Trends Over Months')
        plt.xlabel('Month')
        plt.ylabel('Sales ($)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

    elif type_graph == 'histogram':
        plt.hist(
            df['Sales'],
            bins=4,
            color='green',
            edgecolor='black'
        )
        plt.title('Sales Distribution')
        plt.xlabel('Sales')
        plt.ylabel('Frequency')
        plt.tight_layout()

    elif type_graph == 'piechart':
        plt.pie(
            df['Profit'],
            labels=df['Month'],
            autopct='%1.2f%%',
            startangle=140
        )
        plt.title('Profit Distribution Over Months')

    elif type_graph == 'scatterplot':
        plt.scatter(
            df['Sales'],
            df['Profit'],
            color='green',
            s=100,
            edgecolors='red'
        )
        plt.title('Sales vs Profit Scatter Plot')
        plt.xlabel('Sales')
        plt.ylabel('Profit')
        plt.tight_layout()
        plt.grid(True)

    elif type_graph == 'bargraph':
        width = 0.3

        plt.bar(
            df['Month'],
            df['Sales'],
            width=width,
            color='skyblue',
            label='Sales'
        )

        plt.bar(
            df['Month'],
            df['Profit'],
            width=width,
            color='green',
            label='Profit',
            bottom=df['Sales']
        )

        plt.title('Sales and Profit Trend Over Months')
        plt.xlabel('Month')
        plt.ylabel('Amount ($)')
        plt.legend()
        plt.tight_layout()
        plt.grid(True)

    return fig
