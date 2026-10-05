use world_population;
select `country/territory`, `2000 population`, `2022 population` 
from world_population
where `2000 population` > `2022 population`
order by `2000 population`, `2022 population`
desc

