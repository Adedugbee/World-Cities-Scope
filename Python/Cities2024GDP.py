# Install necessary packages if not already installed
# pip install pandas numpy beautifulsoup4 requests

# Import necessary packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://en.wikipedia.org/wiki/List_of_cities_by_GDP"

# Send HTTP request and parse the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Locate the first relevant table (you may need to adjust if more than one table exists)
table = soup.find("table", {"class": "wikitable"})

# Safety check if table exists
if table:
    rows = table.find_all("tr")

    # Extract data from table rows
    data = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all("td")
        if len(cols) >= 4:
            city = cols[0].text.strip()
            country = cols[1].text.strip()
            gdp = cols[3].text.strip().replace(",", "").replace("$", "")

            # Try converting GDP to float, handle errors gracefully
            try:
                gdp = float(gdp)
            except ValueError:
                gdp = np.nan

            data.append([city, country, gdp])

    # Create DataFrame
    df = pd.DataFrame(data, columns=["City", "Country", "GDP in Billions USD"])

    print(df.head(5))

    # Save to CSV (uncomment if needed)
    # df.to_csv("Cities-GDP.csv", index=False)

else:
    print("GDP table not found on the page.")
