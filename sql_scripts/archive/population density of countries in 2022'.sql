 use world_population;
 select `country/territory`, continent, round(`2022 population` / `Area (kmÂ²)`, 2) as density_2022 
 from world_population
 order by density_2022 desc
 limit 10 