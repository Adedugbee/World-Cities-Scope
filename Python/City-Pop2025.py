# install necessary packages if not already installed
#pip install pandas numpy beautifulsoup4

#import the necessary packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://worldpopulationreview.com/cities"

# Send HTTP request and parse the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Locate the table rows
rows = soup.select("table tbody tr")[:200]  # Select top 200 rows

# Extract rank, city, country, population columns from the table and strip whitespace
data = []
for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 5:
        rank = cols[1].text.strip()
        city = cols[2].text.strip()
        country = cols[3].text.strip()
        population1 = cols[4].text.strip()
        population2 = cols[5].text.strip()
        data.append([rank, country, city, population1, population2])

        # Create DataFrame
df = pd.DataFrame(data, columns=["Rank", "Country", "City", "Population 2025", "Population 2024"])

# Optional: Replace 0s or missing populations with NaN
df[["Population 2025", "Population 2024"]] = df[["Population 2025", "Population 2024"]].replace(0, np.nan)

print(df.head())

# Save to CSV
#df.to_csv("top_200_cities.csv", index=False)