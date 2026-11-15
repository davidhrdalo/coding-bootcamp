-- 28. DELETE and foreign keys
--
-- Remove every cancelled order, together with its order items. Foreign keys are switched on, so the
--     database refuses to delete an order that still has items: delete the children first, then the parents.
--     You need two DELETE statements.
--
-- Write the statements for this exercise (you may use several).
-- Tables: see sql/data/schema.sql. Replace the placeholder below with your answer.

SELECT NULL AS todo;
