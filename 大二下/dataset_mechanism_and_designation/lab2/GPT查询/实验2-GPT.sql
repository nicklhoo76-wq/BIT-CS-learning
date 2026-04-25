SELECT supplier_name, address, phone
FROM Sales.Supplier;

SELECT *
FROM Sales.Orders
WHERE order_date >= '2014-01-01'
  AND order_date <= '2014-10-31'
  AND total_amount > 1000;

SELECT customer_id, SUM(total_amount) AS total_spent
FROM Sales.Orders
GROUP BY customer_id;

SELECT c.customer_id, c.customer_name
FROM Sales.Customer c
JOIN Sales.Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING AVG(o.total_amount) > 1000;

SELECT s.supplier_id, s.supplier_name, s.address
FROM Sales.Supplier s
WHERE s.nation_id = (
    SELECT nation_id
    FROM Sales.Supplier
    WHERE supplier_name = '金仓集团'
);

SELECT p.part_name, p.manufacturer, p.retail_price, ps.supply_price
FROM Sales.Part p
JOIN Sales.PartSupp ps ON p.part_id = ps.part_id
WHERE ps.supply_price > p.retail_price;

SELECT o.order_id, o.total_amount, l.part_id
FROM Sales.Customer c
JOIN Sales.Orders o ON c.customer_id = o.customer_id
JOIN Sales.Lineitem l ON o.order_id = l.order_id
WHERE c.customer_name = '阿波罗';