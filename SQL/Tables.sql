-- The DROP statements were added to prevent errors if the script is mistakenly run more than once
DROP TABLE IF EXISTS top_200_cities;
DROP TABLE IF EXISTS UN_Life_Expectancy;
DROP TABLE IF EXISTS world_gdp_2023_2024;

-- Create the tables
CREATE TABLE top_200_cities (
  `rank` INT PRIMARY KEY,
  `country` VARCHAR(100),
  `city` VARCHAR(100),
  `population_2025` BIGINT,
  `population_2024` BIGINT
);

CREATE TABLE UN_Life_Expectancy (
  `Country` VARCHAR(100),
  `Average Life_Expectancy (UN 2024 Age)` DECIMAL(5,2),
  `Female Life_Expectancy (UN 2024 Age)` DECIMAL(5,2),
  `Male Life_Expectancy (UN 2024 Age)` DECIMAL(5,2)
);

CREATE TABLE world_gdp_2023_2024 (
  country VARCHAR(100),
  gdp_2023 BIGINT,
  gdp_2024 BIGINT
);

