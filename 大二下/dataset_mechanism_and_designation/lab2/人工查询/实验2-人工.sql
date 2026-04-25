SET search_path TO Sales;

SELECT supplier_name, address, phone
FROM Supplier;

SELECT * FROM Orders
WHERE order_date BETWEEN '2013-12-31' AND '2014-11-1'
AND total_amount > 1000;

SELECT Customer.customer_id, SUM(total_amount) AS total_spend
FROM Customer, Orders
WHERE Customer.customer_id = Orders.customer_id
GROUP BY Customer.customer_id;

SELECT customer_id, customer_name
FROM Customer
WHERE customer_id IN (
SELECT customer_id
FROM Orders
GROUP BY customer_id
HAVING AVG(Orders.total_amount) > 1000
);

SELECT supplier_id, supplier_name, address
FROM Supplier
WHERE nation_id = (
SELECT nation_id
FROM Supplier
WHERE supplier_name = '金仓集团'
);

SELECT part_name, manufacturer, retail_price, supply_price
FROM Part, PartSupp
WHERE Part.part_id = PartSupp.part_id AND
supply_price > retail_price;

SELECT Orders.order_id, Orders.total_amount, Lineitem.part_id
FROM Customer, Orders, Lineitem
WHERE Customer.customer_id = Orders.customer_id AND
Orders.order_id = Lineitem.order_id AND
Customer.customer_name = '阿波罗';