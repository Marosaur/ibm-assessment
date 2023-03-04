SELECT o.owner_id, o.owner_name, count(distinct c.category_id) as different_category_count
FROM owner o, article a, category_article_mapping cam, category c
WHERE o.owner_id = a.owner_id
    AND a.article_id = cam.article_id
    AND cam.category_id = c.category_id
ORDER BY different_category_count DESC