SELECT category, ROUND(AVG(price), 2) AS avg_price
    FROM products
    GROUP BY category
    HAVING AVG(price) > 25
    ORDER BY avg_price DESC, category;
