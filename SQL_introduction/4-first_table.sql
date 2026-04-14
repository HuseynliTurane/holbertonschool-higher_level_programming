-- Cari verilənlər bazasında 'first_table' adlı cədvəl yaradır
-- Cədvəlin strukturu:
-- id: INT
-- name: VARCHAR(256)
-- Əgər cədvəl artıq mövcuddursa, skript xəta vermir
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
