SELECT country, COUNT(*) AS customers
    FROM customers
    GROUP BY country
    HAVING COUNT(*) >= 2
    ORDER BY customers DESC, country;
