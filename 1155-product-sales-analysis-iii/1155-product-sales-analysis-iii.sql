# Write your MySQL query statement below
WITH c as (SELECT product_id,MIN(year) as first_year
FROM Sales
GROUP BY product_id
ORDER BY year )

SELECT c.product_id,
        first_year,
        quantity,
        price
FROM Sales
JOIN c
ON sales.product_id=c.product_id
AND sales.year = c.first_year