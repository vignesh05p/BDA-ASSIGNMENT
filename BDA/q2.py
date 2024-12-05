import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with a specified encoding
data = pd.read_csv('norway_new_car_sales_by_model.csv', encoding='ISO-8859-1')

# Create a 'date' column from 'Year' and 'Month'
data['date'] = pd.to_datetime(data[['Year', 'Month']].assign(DAY=1))

# Extract year and month for further analysis
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month

# Specify the year you want to analyze
specified_year = 2012

# Filter data for the specified year and group by month
monthly_sales = data[data['year'] == specified_year].groupby('month')['Quantity'].sum().reset_index()

# Print monthly total car sales
print(monthly_sales)

# Visualize the output using a line chart
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['month'], monthly_sales['Quantity'], marker='o', color='orange')
plt.title(f'Monthly Total Car Sales in Norway for {specified_year}')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(monthly_sales['month'], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid()
plt.show()