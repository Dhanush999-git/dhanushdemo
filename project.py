import pandas as pd
import matplotlib.pyplot as plt

# Load Tesla dataset
tesla = pd.read_csv("TSLA.csv")
tesla['Date'] = pd.to_datetime(tesla['Date'])
tesla['Company'] = "Tesla"

# Load Starbucks dataset (or any second company)
starbucks = pd.read_csv("Starbucks Dataset.csv")
starbucks['Date'] = pd.to_datetime(starbucks['Date'])
starbucks['Company'] = "Starbucks"

# Combine both
df = pd.concat([tesla, starbucks], ignore_index=True)
df.sort_values(by="Date", inplace=True)

# Calculate moving averages
df['7d_MA'] = df.groupby("Company")['Close'].transform(lambda x: x.rolling(7).mean())
df['30d_MA'] = df.groupby("Company")['Close'].transform(lambda x: x.rolling(30).mean())

# Plot both companies
plt.figure(figsize=(14,7))

for company in df['Company'].unique():
    company_data = df[df['Company'] == company]
    plt.plot(company_data['Date'], company_data['Close'], label=f"{company} Close")
    plt.plot(company_data['Date'], company_data['7d_MA'], label=f"{company} 7d MA")
    plt.plot(company_data['Date'], company_data['30d_MA'], label=f"{company} 30d MA")

plt.title("Stock Price Trends: Tesla vs Starbucks")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

# ----- Volatility Comparison -----
print("----- Volatility Comparison -----")
plt.figure(figsize=(12,6))

for company in df['Company'].unique():
    company_data = df[df['Company'] == company].copy()
    returns = company_data['Close'].pct_change().dropna()
    volatility = returns.std()
    print(f"{company}: {volatility:.4f}")
    
    # Plot histogram of daily returns
    plt.hist(returns, bins=50, alpha=0.5, label=f"{company} Returns")

plt.title("Histogram of Daily Returns (Tesla vs Starbucks)")
plt.xlabel("Daily Returns")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()
