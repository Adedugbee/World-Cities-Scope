SELECT 
  c.rank,
  c.city,
  c.country,
  c.population_2024,
  c.population_2025,
  l.`Average Life_Expectancy (UN 2024 Age)`,
  l.`Female Life_Expectancy (UN 2024 Age)`,
  l.`Male Life_Expectancy (UN 2024 Age)`,
  g.gdp_2023,
  g.gdp_2024
FROM top_200_cities c
INNER JOIN UN_Life_Expectancy l
  ON c.country = l.Country
INNER JOIN world_gdp_2023_2024 g
  ON c.country = g.country;
