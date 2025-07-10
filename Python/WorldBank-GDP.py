import requests
import pandas as pd

# API URL and parameters
url = "http://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD"
params = {
    "format": "json",
    "date": "2023:2024",
    "per_page": 10000  # Capture all countries
}

# Make the request
response = requests.get(url, params=params)
data = response.json()

# Check if the response is valid
if not data or len(data) < 2:
    raise ValueError("Failed to fetch data from World Bank API")

# Extract the records (data[1] contains the actual results)
records = data[1]

# Convert to DataFrame
df = pd.DataFrame([{
    "Country": r["country"]["value"],
    "Year": r["date"],
    "GDP": r["value"]
} for r in records if r["value"] is not None])

# Pivot to get GDP for 2023 and 2024 as columns
df_pivot = df.pivot(index="Country", columns="Year", values="GDP").reset_index()
df_pivot.columns.name = None  # remove the 'Year' header from columns

# Renaming columns
df_pivot = df_pivot.rename(columns={"2023": "GDP 2023", "2024": "GDP 2024"})

# Save to CSV
#df_pivot.to_csv("world_gdp_2023_2024.csv", index=False)

print("GDP data saved to 'world_gdp_2023_2024.csv'")
print(df_pivot.head(10))
