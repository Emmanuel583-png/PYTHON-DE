use sql_store;
select concat(customers.first_name, '', customers.last_name) as full_name, sum(order_items.quantity * order_items.unit_price) as total_spend
from customers
left join orders on customers.customer_id = orders.customer_id
left join order_items on orders.order_id = order_items.order_id
group by full_name
order by total_spend desc
limit 5

