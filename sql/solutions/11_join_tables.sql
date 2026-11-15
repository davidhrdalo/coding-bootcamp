SELECT o.id AS order_id, c.name AS customer, p.name AS product, oi.quantity
    FROM orders o
    JOIN customers c ON c.id = o.customer_id
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    WHERE o.status = 'delivered'
    ORDER BY o.id, p.name;
