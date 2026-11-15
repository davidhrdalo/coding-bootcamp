INSERT INTO page_views (page, views) VALUES ('/home', 1)
        ON CONFLICT(page) DO UPDATE SET views = views + 1;
    INSERT INTO page_views (page, views) VALUES ('/new', 1)
        ON CONFLICT(page) DO UPDATE SET views = views + 1;
