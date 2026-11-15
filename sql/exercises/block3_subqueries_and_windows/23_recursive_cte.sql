-- 23. Recursive CTE: an org chart
--
-- List everyone who reports to employee 1, directly or indirectly, with how many steps below
--     employee 1 they are (a direct report has depth 1, a report of a report has depth 2, and so on).
--     Use WITH RECURSIVE. Do not include employee 1 themselves.
--     Show id, name and depth, ordered by depth, then name.
--
-- Result columns, in this order: id, name, depth
-- Write ONE statement: a SELECT (optionally starting with WITH).
-- Tables: see sql/data/schema.sql. Replace the placeholder below with your answer.

SELECT NULL AS todo;
