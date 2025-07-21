SELECT 
  c.rank,
  c.city,
  c.country,
  c.population_2024,
  c.population_2025,
  l.`Average Life_Expectancy (UN 2024 Age)` AS avg_life_expectancy_2024,
  l.`Female Life_Expectancy (UN 2024 Age)` AS female_life_expectancy_2024,
  l.`Male Life_Expectancy (UN 2024 Age)` AS male_life_expectancy_2024,
  g.gdp_2023,
  g.gdp_2024,
  cbg.gdp_billion_usd
FROM top_200_cities c
INNER JOIN cities_by_gdp cbg
  ON c.city = cbg.city
INNER JOIN UN_Life_Expectancy l
  ON c.country = l.country
INNER JOIN world_gdp_2023_2024 g
  ON c.country = g.country;