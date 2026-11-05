
/* Select query to get all locations */
SELECT * FROM locations;

/* Select query to get all members */
SELECT * FROM members;

/* Select query to get all memberships */
SELECT * FROM memberships;

/* Select query to get all employees */
SELECT * FROM employees;

/* Select query to get all roles */
SELECT * FROM roles;

/* Select query to get all products */
SELECT * FROM products;

/* Select query to get all sales */
SELECT * FROM sales;

/* Select query to get sales with product details */
select transaction_id, sales_details_id, quantity, product_id, product_name, product_price
from sales
left join sales_details on sales.transaction_id = sales_details.sales_transaction_id
left join products on sales_details.products_product_id = products.product_id;

/* Select query to get all sales details */
SELECT * FROM sales_details;

/* Insert query to add a sales detail */
/* the %s are placeholders for values that will be passed in */
INSERT INTO sales_details (sales_transaction_id, products_product_id, quantity)
VALUES (%s, %s, %s);

/* Update query to modify the quantity of a sales detail */
UPDATE sales_details
SET quantity = %s
WHERE sales_details_id = %s;

/* Delete a sales detail using its ID */
DELETE FROM sales_details
WHERE sales_details_id = %s;
