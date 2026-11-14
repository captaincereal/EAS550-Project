-- row counts

SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM sellers;
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM order_items;

-- duplicate customer ids

SELECT customer_id, COUNT(*)
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- duplicate order ids

SELECT order_id, COUNT(*)
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- duplicate order item keys

SELECT order_id,
       order_item_id,
       COUNT(*)
FROM order_items
GROUP BY order_id,
         order_item_id
HAVING COUNT(*) > 1;

-- missing customer references

SELECT COUNT(*)
FROM orders o
LEFT JOIN customers c
ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- missing product references

SELECT COUNT(*)
FROM order_items oi
LEFT JOIN products p
ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;

-- missing seller references

SELECT COUNT(*)
FROM order_items oi
LEFT JOIN sellers s
ON oi.seller_id = s.seller_id
WHERE s.seller_id IS NULL;

-- quality check

SELECT COUNT(*)
FROM order_items
WHERE price < 0
OR freight_value < 0;