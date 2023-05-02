DROP TABLE IF EXISTS "times";

-- create the times table
CREATE TABLE IF NOT EXISTS times (
  id SERIAL PRIMARY KEY,
  white FLOAT[],
  black FLOAT[]
);

INSERT INTO times (white) VALUES ('{0.1}');
INSERT INTO times (white) VALUES ('{0.2}');