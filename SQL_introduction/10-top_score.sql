-- 'second_table' cədvəlindəki bütün rekordları siyahılayır
-- Nəticələr 'score' və sonra 'name' sütunlarını göstərir
-- Rekordlar 'score' sütununa görə azalan sıra ilə (ən yüksək bal yuxarıda) düzülür
SELECT score, name FROM second_table ORDER BY score DESC;
