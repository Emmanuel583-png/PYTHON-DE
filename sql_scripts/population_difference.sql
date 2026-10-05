use world_population;
select continent, sum(`2022 population`) - sum(`2000 population`) as population_diff
from world_population
group by continent
order by population_diff desc

