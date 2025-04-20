-- 1. (Optional) Ensure “name” is unique so we can detect conflicts
ALTER TABLE phonebook
  ADD CONSTRAINT phonebook_name_unique UNIQUE (name);


-- 2. Create the upsert procedure
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name  TEXT,
    p_phone TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
  IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
    UPDATE phonebook
       SET phonenumber = p_phone
     WHERE name = p_name;
    RAISE NOTICE '✔ Updated phone for "%" to %', p_name, p_phone;
  ELSE
    INSERT INTO phonebook(name, phonenumber)
         VALUES (p_name, p_phone);
    RAISE NOTICE '✔ Inserted new contact "%" → %', p_name, p_phone;
  END IF;
END;
$$;



-- -- Add Alice if new, or update Alice’s number if she’s already there
-- CALL upsert_contact('Alice', '555-1234');

-- -- Insert Bob
-- CALL upsert_contact('Bob', '555-9876');

-- -- Later, change Alice’s number
-- CALL upsert_contact('Alice', '555-0000');