import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with a specified encoding
data = pd.read_csv('norway_new_car_sales_by_model.csv', encoding='ISO-8859-1')

# Create a 'date' column from 'Year' and 'Month'
data['date'] = pd.to_datetime(data[['Year', 'Month']].assign(DAY=1))

# Extract year and month for further analysis
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month

# a. Print year-wise total car sales and visualize the output
yearly_sales = data.groupby('year')['Quantity'].sum().reset_index()

# Print year-wise total car sales
print(yearly_sales)

# Visualize the output using a bar chart
plt.figure(figsize=(10, 6))
plt.bar(yearly_sales['year'], yearly_sales['Quantity'], color='skyblue')
plt.title('Year-wise Total Car Sales in Norway (2007-2017)')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.xticks(yearly_sales['year'])
plt.show()

# b. Print monthly total car sales and visualize for a specified year
specified_year = 2012
monthly_sales = data[data['year'] == specified_year].groupby('month')['Quantity'].sum().reset_index()

# Print monthly total car sales
print(monthly_sales)

# Visualize the output using a line chart
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['month'], monthly_sales['Quantity'], marker='o', color='orange')
plt.title(f'Monthly Total Car Sales in Norway for {specified_year}')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(monthly_sales['month'])
plt.grid()
plt.show()

# c. Draw pie chart for the sales of all the models of “Toyota” in year 2012
toyota_sales_2012 = data[(data['Make'].str.strip() == 'Toyota') & (data['year'] == 2012)]
model_sales = toyota_sales_2012.groupby('Model')['Quantity'].sum().reset_index()

# Draw pie chart
plt.figure(figsize=(8, 8))
plt.pie(model_sales['Quantity'], labels=model_sales['Model'], autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution of Toyota Models in 2012')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()

# d. Compare Car models with Percentage shares
model_sales = data.groupby('Model')['Quantity'].sum().reset_index()
model_sales['Pct'] = (model_sales['Quantity'] / model_sales['Quantity'].sum()) * 100

# Print percentage shares
print(model_sales)

# Visualize the percentage shares using a bar chart
plt.figure(figsize=(12, 6))
plt.bar(model_sales['Model'], model_sales['Pct'], color='lightgreen')
plt.title('Percentage Share of Car Models')
plt.xlabel('Car Model')
plt.ylabel('Percentage Share (%)')
plt.xticks(rotation=90)
plt.show()