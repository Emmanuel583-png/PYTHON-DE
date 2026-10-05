use world_population;
select continent, avg(`2022 population`)
from world_population
group by continent
order by avg(`2022 population`) desc