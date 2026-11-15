WITH spend AS (
        SELECT c.id, c.name, ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_spent
        FROM customers c
        JOIN orders o ON o.customer_id = c.id AND o.status <> 'cancelled'
        JOIN order_items oi ON oi.order_id = o.id
        GROUP BY c.id, c.name
    )
    SELECT name, total_spent
    FROM spend
    WHERE total_spent > (SELECT AVG(total_spent) FROM spend)
    ORDER BY total_spent DESC, name;
