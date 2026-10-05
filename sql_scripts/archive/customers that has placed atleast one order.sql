use sql_store;
select concat(customers.first_name, ' ' , customers.last_name) as full_name, count(orders.order_id) as total_orders, customers.points
from customers
inner join orders on customers.customer_id = orders.customer_id
group by customers.customer_id 
having count(orders.order_id) >= 1
order by total_orders desc 