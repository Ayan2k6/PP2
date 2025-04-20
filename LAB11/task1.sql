-- 1) Create (or replace) the search function
CREATE OR REPLACE FUNCTION search_phonebook(p_pattern TEXT)
RETURNS TABLE (
    id INTEGER,
    name VARCHAR,
    phonenumber VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, phonenumber
    FROM phonebook
    WHERE name ILIKE '%' || p_pattern || '%'
       OR phonenumber LIKE '%' || p_pattern || '%';
END;
$$
LANGUAGE plpgsql;



-- -- Find everyone whose name contains “ann” (case‑insensitive):
-- SELECT * FROM search_phonebook('ann');

-- -- Find any contact with “123” in their phone number:
-- SELECT * FROM search_phonebook('123');
