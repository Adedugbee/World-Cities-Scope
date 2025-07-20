from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import re

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_cities_by_GDP"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the main GDP table (first table with 'wikitable' class)
table = soup.find("table", {"class": "wikitable"})

# List to store rows
data = []

# Check if table exists
if table:
    rows = table.find_all("tr")

    for row in rows[1:]:  # Skip header
        cols = row.find_all(["td", "th"])
        col_text = [col.get_text(strip=True) for col in cols]

        # Ensure the row has enough columns (at least 3)
        if len(col_text) >= 3:
            city = col_text[0]
            city = re.sub(r"\s*\([^)]*\)|\s*\[[^\]]*\]", "", city)  # remove (...) and [...]
            city = city.split(",")[0]  # remove comma and everything after
            city = city.strip()

            country = col_text[1]

            gdp_raw = col_text[2]

            # Clean GDP string: remove (2021), [5], etc.
            gdp_cleaned = re.sub(r"\s*\([^)]*\)|\s*\[[^\]]*\]", "", gdp_raw)

            # Attempt to convert GDP to float
            try:
                gdp = float(gdp_cleaned.replace(",", ""))
            except ValueError:
                gdp = np.nan

            data.append([city, country, gdp])

    # Create DataFrame
    df = pd.DataFrame(data, columns=["City (proper/metropolitan area)", "Country/Region", "GDP (Billions USD)"])

    # Show top 5 rows
    print(df.head(5))

    # Save to CSV
    df.to_csv("cities_by_gdp.csv", index=False)

else:
    print("No table found on the page.")
