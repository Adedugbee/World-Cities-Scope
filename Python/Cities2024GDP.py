# install necessary packages if not already installed
#pip install pandas numpy beautifulsoup4

#import the necessary packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://en.wikipedia.org/wiki/List_of_cities_by_GDP"

# Send HTTP request and parse the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Locate the table rows
rows = soup.select("table tbody tr")[0:]  # Select all rows

# Extract rank, city, country, population columns from the table and strip whitespace
data = []
for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 3:
        cities = cols[1].text.strip()
        country = cols[2].text.strip()
        gdp = cols[3].text.strip()
        data.append([cities, country,gdp])

        # Create DataFrame
df = pd.DataFrame(data, columns=["Cities", "Country","GDP in Millions USD"])

# Replace 0s or missing populations with NaN
df[["GDP in Millions USD"]] = df[["GDP in Millions USD"]].replace(0, np.nan)

print(df.head(5))

# Save to CSV
#df.to_csv("Cities-GDP", index=False)