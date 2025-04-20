-- 1) Create (or replace) the delete procedure
CREATE OR REPLACE PROCEDURE delete_contact(
    IN  p_name   TEXT DEFAULT NULL,
    IN  p_phone  TEXT DEFAULT NULL,
    OUT deleted_count  INT
)
LANGUAGE plpgsql
AS $$
BEGIN
  -- Must supply exactly one criterion
  IF (p_name IS NULL AND p_phone IS NULL)
     OR (p_name IS NOT NULL AND p_phone IS NOT NULL)
  THEN
    RAISE EXCEPTION 
      'Please supply exactly one of p_name or p_phone (got name=%, phone=%)',
      p_name, p_phone;
  END IF;

  IF p_name IS NOT NULL THEN
    DELETE FROM phonebook
     WHERE name = p_name;
    GET DIAGNOSTICS deleted_count = ROW_COUNT;
  ELSE
    DELETE FROM phonebook
     WHERE phonenumber = p_phone;
    GET DIAGNOSTICS deleted_count = ROW_COUNT;
  END IF;
END;
$$;






-- -- Delete by name:
-- CALL delete_contact('Alice', NULL, deleted_rows);
-- -- PostgreSQL will then display:
-- --  deleted_rows 
-- -- --------------
-- --            1

-- -- Delete by phone:
-- CALL delete_contact(NULL, '5551234567', deleted_rows);
-- --  deleted_rows 
-- -- --------------
-- --            2

-- -- Bad usage (both NULL):
-- CALL delete_contact(NULL, NULL, deleted_rows);
-- -- ERROR:  Please supply exactly one of p_name or p_phone (got name=, phone=)

-- -- Bad usage (both set):
-- CALL delete_contact('Bob', '5550000', deleted_rows);
-- -- ERROR:  Please supply exactly one of p_name or p_phone (got name=Bob, phone=5550000)
