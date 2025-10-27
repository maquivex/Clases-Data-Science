--- SENTENCIAS DDL ---
--- CREATE TABLE TEMPLATE ---
CREATE TABLE alumno(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    nro_documento varchar(15) NOT NULL,
    nombre varchar(255) NOT NULL,
    email varchar(255)
);

--- MODIFICAR UNA TABLA ---
ALTER TABLE alumno 
ADD COLUMN nota INT DEFAULT 0;

--- ELIMINAR UNA TABLA ---
DROP TABLE alumno;

