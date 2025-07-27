# Urban Metrics Data Engineering Project
This project demonstrates an end-to-end data engineering workflow for analyzing global urban trends. The top 200 cities by population were scraped from World Population Review, country-level life expectancy data was collected from the same source, **GDP** figures for **2023** and **2024** were retrieved via the **World Bank API**, and city-level **GDP** data was extracted from Wikipedia. Majority of the data were cleaned with python before the final manual cleaning the output CSV files.

Using Python tools such as Pandas, BeautifulSoup, and Requests, the datasets were cleaned, normalized, and saved as **CSV** files. These files were then imported into a **MySQL** relational database, where the schema was designed to support relational joins and analytical transformations.

SQL was used to create unified views and materialized tables that calculate:

* Year-over-year population growth

* GDP growth at both city and country levels

* City GDP as a share of national GDP

* GDP per capita for each city

A final dataset of 103 cleaned city records was exported and visualized in **Google Looker Studio**, offering insights into the relationship between population trends, economic size, and life expectancy.
