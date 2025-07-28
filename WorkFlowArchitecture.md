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

* Convert numerical columns to proper data types (e.g., int, float).

* Clean Wikipedia city names (remove footnotes/superscripts using regex).

* Validate consistency between city/country names across datasets.


# 3. Data Storage Layer (MySQL)
## Schema Definition:
#### Tables created using the following DDL (Data Definition Language):
[Create Table](https://github.com/Adedugbee/World-Cities-Scope/blob/main/SQL/Tables.sql)

## CSVs imported into MySQL:
* Used MySQL Workbench import.

* Manual review before importing cities_by_gdp to ensure clean and accurate matching.


# 4. Data Integration
## Inner Join Query:
Combined all datasets into one integrated view using matching columns:
[Inner Join](https://github.com/Adedugbee/World-Cities-Scope/blob/main/SQL/Inner_Join_All_Tables.sql)

## Materialized View:
Created for performance optimization:
[MQT](https://github.com/Adedugbee/World-Cities-Scope/blob/main/SQL/Materialized_View.sql)


# 5. Analytical Calculations
[Complex metrics included](https://github.com/Adedugbee/World-Cities-Scope/blob/main/SQL/city_population_gdp_analysis.sql):

### Snippet
- Population growth (%):
 (population_2025 - population_2024) / population_2024 * 100

* GDP change (%):
 (gdp_2024 - gdp_2023) / gdp_2023 * 100

* City GDP as % of national GDP:

  * 2023: (city_gdp / country_gdp_2023)
  * 2024: (city_gdp / country_gdp_2024)

* GDP per capita:
 (city_gdp * 1B) / population_2024
