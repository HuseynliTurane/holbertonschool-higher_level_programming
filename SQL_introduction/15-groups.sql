-- Eyni balı toplayan rekordların sayını siyahılayır
-- Nəticədə 'score' və rekordların sayı 'number' etiketi ilə göstərilir
-- Siyahı rekordların sayına görə azalan sıra ilə düzülür
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
