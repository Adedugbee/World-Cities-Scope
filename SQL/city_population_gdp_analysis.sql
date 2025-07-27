-- Analyze population growth, GDP change, GDP share, and per capita GDP for top cities
-- This query retrieves key metrics for cities including population figures for 2024 and 2025,
-- life expectancy data, GDP in billion USD, and calculates percentage changes and per capita GDP.
-- The calculations include:
-- 1. Population change from 2024 to 2025 as a percentage.
-- 2. GDP change from 2023 to 2024 as a percentage.
-- 3. The city's GDP as a percentage of the total GDP for 2023 and 2024.
-- 4. GDP per capita for the year 2024.
-- The data is sourced from the `city_life_gdp_mv` materialized view.
-- The result is sorted by the city's rank and exported for further analysis.

-- 
SELECT 
`rank`,
city,
country,
population_2024,
population_2025,
avg_life_expectancy_2024,
female_life_expectancy_2024,
male_life_expectancy_2024,
gdp_billion_usd as city_gdp_billion_usd,
gdp_2023 as country_gdp_2023,
gdp_2024 as country_gdp_2024,
ROUND(((population_2025 - population_2024) / population_2024) * 100, 2) AS '2024_2025_population_change (%)',
Round(((gdp_2024 - gdp_2023) / gdp_2023) * 100, 2) AS '2023_2024_gdp_change (%)',
Round((((gdp_billion_usd) *1000000000) / gdp_2023) * 100, 2) AS percent_of_total_2023_gdp,
Round((((gdp_billion_usd) *1000000000) / gdp_2024) * 100, 2) AS percent_of_total_2024_gdp,
Round((((gdp_billion_usd) *1000000000)/ population_2024), 2) AS 'gdp_per_capita (2024)'
FROM city_life_gdp_mv 
ORDER BY `Rank`;

SELECT COUNT(*) FROM city_life_gdp_mv;





