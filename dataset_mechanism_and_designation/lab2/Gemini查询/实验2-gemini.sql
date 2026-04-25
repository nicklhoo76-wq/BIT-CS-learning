-- 1）查询所有供应商的名称、地址、联系电话。
SELECT 
    supplier_name, 
    address, 
    phone 
FROM Sales.Supplier;

-- 2）查询2014年1~10月间的总价大于1000元的订单的编号、顾客编号等订单的所有信息。
SELECT * FROM Sales.Orders 
WHERE order_date BETWEEN '2014-01-01' AND '2014-10-31'
  AND total_amount > 1000;

-- 3）统计每个顾客的订购金额（假设包括没有订单的顾客，显示为0或NULL）。
SELECT 
    c.customer_id, 
    c.customer_name, 
    SUM(o.total_amount) AS total_spent
FROM Sales.Customer c
LEFT JOIN Sales.Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name;

-- 4）查询订单平均金额超过1000元的顾客编号及其姓名。
SELECT 
    c.customer_id, 
    c.customer_name
FROM Sales.Customer c
JOIN Sales.Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING AVG(o.total_amount) > 1000;

-- 5）查询与“金仓集团”在同一个国家的供应商编号、名称和地址信息（排除金仓集团本身）。
SELECT 
    supplier_id, 
    supplier_name, 
    address
FROM Sales.Supplier
WHERE nation_id = (
    SELECT nation_id 
    FROM Sales.Supplier 
    WHERE supplier_name = '金仓集团'
)
AND supplier_name <> '金仓集团';

-- 6）查询供应价格大于零售价格的零件名、制造商名、零售价格和供应价格。
SELECT 
    p.part_name, 
    p.manufacturer, 
    p.retail_price, 
    ps.supply_price
FROM Sales.Part p
JOIN Sales.PartSupp ps ON p.part_id = ps.part_id
WHERE ps.supply_price > p.retail_price;

-- 7）查询顾客“阿波罗”订购的订单编号、总价及其订购的零件编号。
SELECT 
    o.order_id, 
    o.total_amount, 
    l.part_id
FROM Sales.Customer c
JOIN Sales.Orders o ON c.customer_id = o.customer_id
JOIN Sales.Lineitem l ON o.order_id = l.order_id
WHERE c.customer_name = '阿波罗';