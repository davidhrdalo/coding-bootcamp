-- 29. UPSERT (INSERT ... ON CONFLICT)
--
-- The page_views table counts visits per page (page is the primary key). Record one visit to '/home'
--     and one visit to '/new' using INSERT ... ON CONFLICT(page) DO UPDATE, so that:
--       - an existing page has its views increased by 1
--       - a page that does not exist yet is created with views = 1
--     Use two INSERT statements (one per page).
--
-- Write the statements for this exercise (you may use several).
-- Tables: see sql/data/schema.sql. Replace the placeholder below with your answer.

SELECT NULL AS todo;
