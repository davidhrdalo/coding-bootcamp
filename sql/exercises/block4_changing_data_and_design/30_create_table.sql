-- 30. CREATE TABLE with constraints
--
-- Create a table called reviews with these columns, in this order:
--       id          INTEGER, the primary key
--       product_id  INTEGER, required, references products(id)
--       customer_id INTEGER, required, references customers(id)
--       rating      INTEGER, required, must be between 1 and 5
--       comment     TEXT, optional
--       created_at  TEXT, required, defaults to the current date (DEFAULT CURRENT_DATE)
--     The checks insert some rows to make sure your constraints really work.
--
-- Write the statements for this exercise (you may use several).
-- Tables: see sql/data/schema.sql. Replace the placeholder below with your answer.

SELECT NULL AS todo;
