use sql_store;
select order_items.product_id, products.name
from products
left join order_items on products.product_id = order_items.product_id
where order_items.product_id is null