# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:\RAKESH\Internships\InnoByte\Code\Amazon Sale Report.csv"  # Replace with your file path
data = pd.read_csv(file_path)

# Convert "Date" to datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Drop rows with invalid dates
data = data.dropna(subset=['Date'])

# Add a "Month" column for monthly aggregation
data['Month'] = data['Date'].dt.to_period('M')

# Sales Overview: Monthly Sales Trend
monthly_sales = data.groupby('Month')['Amount'].sum()
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color='blue')
plt.title('Monthly Sales Trend', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales Amount (INR)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Category Analysis: Top Product Categories by Sales
category_sales = data.groupby('Category')['Amount'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar', color='orange', alpha=0.8)
plt.title('Top Product Categories by Sales', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales Amount (INR)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Geographical Analysis: Top States by Sales
state_sales = data.groupby('ship-state')['Amount'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
state_sales.head(10).plot(kind='bar', color='green', alpha=0.8)
plt.title('Top States by Sales', fontsize=16)
plt.xlabel('State', fontsize=12)
plt.ylabel('Total Sales Amount (INR)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Customer Segmentation: Top Customers by Total Spend
customer_spend = data.groupby('Order ID')['Amount'].sum().sort_values(ascending=False)
print("Top 10 Customers by Total Spend:")
print(customer_spend.head(10))
