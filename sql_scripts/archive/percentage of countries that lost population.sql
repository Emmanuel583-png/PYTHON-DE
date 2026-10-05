use world_population;
select continent, count(*) as total_countries, 
sum(case when `2022 population` < `2000 population` then 1 else 0 end) as countries_lost_ppl,
round((sum(case when `2022 population` < `2000 population` then 1 else 0 end) / count(*)) * 100, 2) as percentage_lost
from world_population
group by continent
order by percentage_lost desc

