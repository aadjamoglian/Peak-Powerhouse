-- Active: 1793586391018@@127.0.0.1@3306@peak_ph_db
select * from locations;

select transaction_id, sales_details_id, quantity, product_id, product_name, product_price
from sales
left join sales_details on sales.transaction_id = sales_details.sales_transaction_id
left join products on sales_details.products_product_id = products.product_id

select * from sales_details;