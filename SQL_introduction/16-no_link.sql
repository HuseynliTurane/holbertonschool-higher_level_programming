-- 'second_table' cədvəlində adı olan bütün rekordları siyahılayır
-- 'name' dəyəri olmayan (NULL və ya boş) sətirləri göstərmir
-- Nəticələr score və name (bu ardıcıllıqla) sütunlarını göstərir
-- Rekordlar score-a görə azalan sıra ilə düzülür
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
