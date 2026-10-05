use sql_store;
select concat(first_name,' ', last_name ) as full_name, points
from customers
where points > (select avg(points) from customers)
order by points desc

