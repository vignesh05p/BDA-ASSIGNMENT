import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with a specified encoding
data = pd.read_csv('norway_new_car_sales_by_model.csv', encoding='ISO-8859-1')

# Create a 'date' column from 'Year' and 'Month'
data['date'] = pd.to_datetime(data[['Year', 'Month']].assign(DAY=1))

# Extract year and month for further analysis
data['year'] = data['date'].dt.year

# Specify the year you want to analyze
specified_year = 2012

# Filter data for Toyota models in the specified year
toyota_sales_2012 = data[(data['Make'].str.strip() == 'Toyota') & (data['year'] == specified_year)]

# Group by model and sum the sales quantities
model_sales = toyota_sales_2012.groupby('Model')['Quantity'].sum().reset_index()

# Draw pie chart
plt.figure(figsize=(8, 8))
plt.pie(model_sales['Quantity'], labels=model_sales['Model'], autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution of Toyota Models in 2012')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()