-- 31. Indexes and query plans
--
-- Add indexes so these two queries stop scanning whole tables:
--       1. SELECT * FROM orders WHERE customer_id = 3
--       2. SELECT name FROM products WHERE category = 'Books' ORDER BY price
--     The first needs an index on orders(customer_id). The second can use ONE index on both columns, in
--     the right order, so the database can find the category AND read the rows already sorted by price
--     (no separate sort step). The checks look at SQLite's EXPLAIN QUERY PLAN output.
--     Give your indexes any names you like.
--
-- Write the statements for this exercise (you may use several).
-- Tables: see sql/data/schema.sql. Replace the placeholder below with your answer.

SELECT NULL AS todo;
