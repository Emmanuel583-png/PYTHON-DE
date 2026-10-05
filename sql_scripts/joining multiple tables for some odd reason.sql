use sql_store;
select orders.order_id, customers.first_name, shippers.name, orders.status 
from orders 
inner join customers on orders.customer_id = customers.customer_id
inner join shippers on orders.shipper_id = shippers.shipper_id