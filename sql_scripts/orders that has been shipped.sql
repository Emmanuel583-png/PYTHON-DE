use sql_store;
select concat(customers.first_name, ' ', customers.last_name) as full_name, orders.order_date, shippers.name, orders.shipper_id
from customers
left join orders on customers.customer_id = orders.customer_id
left join shippers on orders.shipper_id = shippers.shipper_id  
where orders.shipper_id is not null
order by order_date desc
