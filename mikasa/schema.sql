DROP TABLE IF EXISTS ropa;


CREATE TABLE ropa (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tipo text NOT NULL,
  descripcion TEXT UNIQUE NOT NULL,
  costo INTEGER NOT NULL,
  veces INTEGER default 1,
  uso NUMERIC,
  modificado datetime default current_timestamp,
  dt datetime default current_timestamp,
  comentarios text
);