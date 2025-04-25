import pandas as pd
from datetime import datetime

# Create different types of datetime objects
print("a) Date object for Jan 15, 2012:", pd.Timestamp("2012-01-15"))
print("b) Specific time 9:20 PM:", pd.Timestamp("2025-04-25 21:20:00"))
print("c) Local date and time:", pd.Timestamp.now())
print("d) Date without time:", pd.Timestamp.today().date())
print("e) Current date:", pd.Timestamp.today().normalize())
print("f) Time from now:", pd.Timestamp.now().time())
print("g) Current local time:", datetime.now().time())
