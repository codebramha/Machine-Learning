import pandas as pd
import quandl
df = quandl.get("WIKI/GOOGL", authtoken="6PjDgg8AVsE5KYE9H-Lz")
print(df.head())