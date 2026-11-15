SELECT name, price,
           CASE WHEN price < 10 THEN 'budget'
                WHEN price < 50 THEN 'standard'
                ELSE 'premium' END AS tier
    FROM products
    ORDER BY price, name;
