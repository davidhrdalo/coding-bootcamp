SELECT p.name AS product, SUM(oi.quantity) AS units
    FROM order_items oi
    JOIN orders o ON o.id = oi.order_id AND o.status <> 'cancelled'
    JOIN products p ON p.id = oi.product_id
    GROUP BY p.id, p.name
    ORDER BY units DESC, product
    LIMIT 3;
