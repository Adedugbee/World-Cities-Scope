# 1. Data Ingestion Layer
## Web Scraping and API Access

| Source                                                                                                                                | Method                                           | Description                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------ |
| [worldpopulationreview.com/cities](https://worldpopulationreview.com/cities)                                                          | Web scraping (e.g., `BeautifulSoup`, `Selenium`) | Extract top 200 cities with population forecasts for 2024 and 2025 |
| [worldpopulationreview.com/life-expectancy-by-country](https://worldpopulationreview.com/country-rankings/life-expectancy-by-country) | Web scraping                                     | Scrape average, male, and female life expectancy data by country   |
| [api.worldbank.org](http://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD)                                                 | API calls (e.g., `requests`)                     | Get GDP data (2023 & 2024) per country                             |
| [Wikipedia - Cities by GDP](https://en.wikipedia.org/wiki/List_of_cities_by_GDP)                                                      | Web scraping + manual cleaning                   | GDP per city in billions of USD                                    |

## Output: Raw data as pandas DataFrames, saved to CSVs

# 2. Data Cleaning & Transformation
## Common Steps:
Normalize and clean column names.

*Convert numerical columns to proper data types (e.g., int, float).

*Clean Wikipedia city names (remove footnotes/superscripts using regex).

*Validate consistency between city/country names across datasets.
