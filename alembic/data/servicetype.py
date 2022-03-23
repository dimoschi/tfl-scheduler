SERVICE_TYPE_INITIAL = """
    INSERT INTO servicetype(id, name)
    VALUES ('regular', 'Regular'),  ('night', 'Night');"""

SERVICE_TYPE_TRUNCATE = "TRUNCATE servicetype RESTART IDENTITY CASCADE;"
