-- 4) Create (or replace) a pagination function
CREATE OR REPLACE FUNCTION get_phonebook_page(
  p_limit  INT,
  p_offset INT
)
  RETURNS TABLE (
    id          INT,
    name        VARCHAR,
    phonenumber VARCHAR
  )
LANGUAGE sql
AS $$
  SELECT id, name, phonenumber
    FROM phonebook
   ORDER BY id
   LIMIT p_limit
  OFFSET p_offset;
$$;




-- -- Get the first 5 contacts
-- SELECT * FROM get_phonebook_page(5, 0);

-- -- Get the next 5 (rows 6–10)
-- SELECT * FROM get_phonebook_page(5, 5);

-- -- Get 10 rows starting at row 20
-- SELECT * FROM get_phonebook_page(10, 20);
