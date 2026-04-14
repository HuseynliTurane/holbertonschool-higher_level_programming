-- 'second_table' cədvəlində score >= 10 olan rekordları siyahılayır
-- Nəticələr score və name (bu ardıcıllıqla) sütunlarını göstərir
-- Rekordlar score-a görə azalan sıra ilə düzülür
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
