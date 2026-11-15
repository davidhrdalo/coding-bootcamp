WITH monthly AS (
        SELECT strftime('%Y-%m', o.order_date) AS month,
               ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
        FROM orders o
        JOIN order_items oi ON oi.order_id = o.id
        WHERE o.status <> 'cancelled'
        GROUP BY month
    )
    SELECT month, revenue, ROUND(SUM(revenue) OVER (ORDER BY month), 2) AS running_total
    FROM monthly
    ORDER BY month;
