-- This query retrieves city-level demographic and economic metrics from the 'city_life_gdp_mv' view.
-- It calculates the following derived fields for each city:
-- 1. population_change: The percentage increase or decrease in population from 2024 to 2025, rounded to 2 decimal places.
-- 2. gdp_change: The percentage change in GDP from 2023 to 2024, also rounded to 2 decimal places.
-- 3. gdp_per_capita (2024): The GDP per capita for 2024, computed by dividing total GDP by population, rounded to 2 decimal places.
-- The result is sorted by the city's rank for easier interpretation or reporting.

SELECT *, 
  ROUND(((population_2025 - population_2024) / population_2024) * 100, 2) AS population_change,
  ROUND(((gdp_2024 - gdp_2023) / gdp_2023) * 100, 2) AS gdp_change,
  ROUND((gdp_2024 / population_2024), 2) AS 'gdp_per_capita (2024)'
FROM city_life_gdp_mv
ORDER BY `Rank`;
