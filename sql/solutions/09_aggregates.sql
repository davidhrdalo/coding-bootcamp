SELECT COUNT(*) AS order_count,
           COUNT(DISTINCT customer_id) AS customers_with_orders,
           MIN(order_date) AS first_order,
           MAX(order_date) AS last_order
    FROM orders;
