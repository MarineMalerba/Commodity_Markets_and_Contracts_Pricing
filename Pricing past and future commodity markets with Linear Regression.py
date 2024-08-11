import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression 
import numpy as np
from pandas.tseries.offsets import DateOffset

# Load the data from the uploaded CSV file into a DataFrame
file_path = '' #insert path to 'Nat_Gas.csv'
df = pd.read_csv(file_path)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df['Dates'], df['Prices'], marker='o')
plt.title('Monthly Natural Gas Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# Prepare data for Linear Regression
df['Dates'] = pd.to_datetime(df['Dates'])
df['Month'] = df['Dates'].dt.month
df['Year'] = df['Dates'].dt.year

# Function to estimate price for any given date
def estimate_price(date):
    target_date = datetime.strptime(date, '%m/%d/%y')
    target_month = target_date.month
    
    # Filter data for the same month in previous years
    month_data = df[df['Month'] == target_month]
    
    # Prepare data for Linear Regression
    month_data['Date_ordinal'] = month_data['Dates'].map(datetime.toordinal)
    X = month_data[['Date_ordinal']]
    Y = month_data['Prices']
    
    # Fit Linear Regression model
    model = LinearRegression()
    model.fit(X, Y)
    
    # Predict the price for the target date
    target_date_ordinal = target_date.toordinal()
    estimated_price = model.predict([[target_date_ordinal]])
    
    return estimated_price[0]

# Example usage
date_to_estimate = '10/31/26'
estimated_price = estimate_price(date_to_estimate)
print(f"Estimated price on {date_to_estimate}: {estimated_price:.2f}")

# Predict for the next 12 months
future_dates = [df['Dates'].max() + pd.DateOffset(months=i) for i in range(1, 13)]
future_prices = [estimate_price(date.strftime('%m/%d/%y')) for date in future_dates]

# Store future predictions in a DataFrame
future_df = pd.DataFrame({'Dates': future_dates, 'Prices': future_prices})

# Plot the original data and future predictions
plt.figure(figsize=(12, 6))
plt.plot(df['Dates'], df['Prices'], marker='o', label='Historical Prices')
plt.plot(future_df['Dates'], future_df['Prices'], marker='o', linestyle='--', label='Future Predictions')
plt.title('Natural Gas Prices with Future Predictions')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
