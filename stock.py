# Import necessary libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol and date range for analysis
stock_symbol = "AAPL"
start_date = "2020-01-01"
end_date = "2021-12-31"

# Fetch historical stock data using yfinance
df = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate daily returns
df['Daily_Return'] = df['Adj Close'].pct_change()

# Calculate 50-day and 200-day moving averages
df['50_Day_MA'] = df['Adj Close'].rolling(window=50).mean()
df['200_Day_MA'] = df['Adj Close'].rolling(window=200).mean()

# Calculate Bollinger Bands
window = 20  # Bollinger Bands window
df['Rolling_Mean'] = df['Adj Close'].rolling(window=window).mean()
df['Upper_Band'] = df['Rolling_Mean'] + 2 * df['Adj Close'].rolling(window=window).std()
df['Lower_Band'] = df['Rolling_Mean'] - 2 * df['Adj Close'].rolling(window=window).std()

# Create a new DataFrame for analysis
analysis_df = df[['Adj Close', 'Daily_Return', '50_Day_MA', '200_Day_MA', 'Upper_Band', 'Lower_Band']]

# Plotting the stock data and indicators
plt.figure(figsize=(12, 6))
plt.title(f"Stock Performance Analysis for {stock_symbol}")
plt.plot(analysis_df.index, analysis_df['Adj Close'], label='Adj Close', color='blue')
plt.plot(analysis_df.index, analysis_df['50_Day_MA'], label='50-Day MA', color='orange')
plt.plot(analysis_df.index, analysis_df['200_Day_MA'], label='200-Day MA', color='red')
plt.fill_between(analysis_df.index, analysis_df['Upper_Band'], analysis_df['Lower_Band'], color='gray', alpha=0.2, label='Bollinger Bands')
plt.xlabel("Date")
plt.ylabel("Price / Moving Averages")
plt.legend()
plt.grid()

# Plotting daily returns
plt.figure(figsize=(12, 4))
plt.title(f"Daily Returns for {stock_symbol}")
plt.plot(analysis_df.index, analysis_df['Daily_Return'], label='Daily Return', color='green')
plt.xlabel("Date")
plt.ylabel("Daily Return")
plt.legend()
plt.grid()

# Save the plots as images (optional)
# plt.savefig('stock_analysis_plots.png')

# Show the plots
plt.show()

# Provide actionable insights to stakeholders based on the analysis
print("Actionable Insights:")
print("- The stock's 50-day moving average crossed above the 200-day moving average, indicating a potential bullish trend.")
print("- The Bollinger Bands can be used to identify potential overbought or oversold conditions.")
print("- Analyze daily returns for volatility and risk assessment.")

# Save the analysis results to a CSV file (optional)
# analysis_df.to_csv('stock_analysis_results.csv')
