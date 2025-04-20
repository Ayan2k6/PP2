-- 1) Define a composite type to hold one contact’s data
CREATE TYPE contact_input AS (
  name        TEXT,
  phonenumber TEXT
);


-- 2) Create the “bulk insert” procedure
--    - IN  p_contacts     : an array of contact_input records
--    - OUT invalid_contacts : returns an array of those input records whose phone failed validation
CREATE OR REPLACE PROCEDURE insert_many_contacts(
  IN  p_contacts        contact_input[],
  OUT invalid_contacts  contact_input[]
)
LANGUAGE plpgsql
AS $$
DECLARE
  rec            contact_input;
  bad_list       contact_input[] := '{}';
BEGIN
  FOREACH rec IN ARRAY p_contacts LOOP
    -- simple phone‐format check: exactly 10 digits
    IF rec.phonenumber ~ '^[0-9]{10}$' THEN
      -- reuse the upsert from Task 2
      CALL upsert_contact(rec.name, rec.phonenumber);
    ELSE
      -- collect invalid entries
      bad_list := array_append(bad_list, rec);
    END IF;
  END LOOP;

  invalid_contacts := bad_list;
END;
$$;






-- How to invoke

-- -- Prepare a little test set, mixing valid & invalid phones:
-- CALL insert_many_contacts(
--   ARRAY[
--     ROW('Alice','5551234567')::contact_input,
--     ROW('Bob',  '123‑X456789')::contact_input,
--     ROW('Carol','9876543210')::contact_input,
--     ROW('Dan',  'phone12345')::contact_input
--   ]  
--   ,   -- capture the OUT array into a variable:
--   ARRAY[]::contact_input[]  -- passing an “empty” placeholder
-- )  
-- INTO   -- here ‘invalids’ will hold Bob & Dan
--   invalids;

-- -- See what didn’t make it:
-- SELECT * FROM unnest(invalids) AS t(name, phonenumber);
