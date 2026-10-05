use sql_invoicing;
select clients.name, sum(invoices.invoice_total - invoices.payment_total) as total_unpaid
from clients 
left join invoices on clients.client_id = invoices.client_id
group by clients.name
having sum(invoices.payment_total = 0) > 0
order by total_unpaid desc