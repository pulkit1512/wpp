import pandas as pd

# Example data
asking_prices = pd.Series([25000, 18000, 30000, 22000])
fair_prices = pd.Series([26000, 20000, 28000, 23000])

# Find indices of good deals
good_deal_indices = asking_prices[asking_prices < fair_prices].index.tolist()
print("Good deals at indices:", good_deal_indices)
