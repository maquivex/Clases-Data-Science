--- SENTENCIAS DML ---

--- CRUD 
--- C - INSERT
--- R - SELECT
--- U - UPDATE  
--- D - DELETE

--- INSERT

INSERT INTO alumno (nro_documento, nombre, email) VALUES ('12345678', 'Juan Perez', 'askss@correo.com');

--- INSERTAR VARIOS REGISTROS

INSERT INTO alumno (nro_documento, nombre, email) 
VALUES 
('87654321', 'Maria Gomez', 'maria@correo.com'),
('11223344', 'Carlos Ruiz', 'carlos@correo.com'),
('44332211', 'Ana Lopez', 'ana@correo.com'),
('55667788', 'Luis Fernandez', 'luis@correo.com'),
('99887766', 'Sofia Martinez', 'sofia@correo.com'),
('66778899', 'Diego Torres', 'diego@correo.com'),
('33445566', 'Elena Ramirez', 'elena@correo.com'),
('22113344', 'Jorge Sanchez', 'jorge@correo.com'),
('77889900', 'Laura Diaz', 'laura@correo.com'),
('44556677', 'Miguel Herrera', 'miguel@correo.com'),
('88990011', 'Natalia Castro', 'natalia@correo.com'),
('11224433', 'Andres Morales', 'andres@correo.com'),
('33446655', 'Valeria Jimenez', 'valeria@correo.com');

--- ACTUALIZAR DATOS (UPDATE)
UPDATE alumno set email = 'codigo@correo.com';

--- ACTUALIZAR CON CONDIOCIONAL
UPDATE alumno set email = 'nuevo@correo.com' WHERE id = 1;

--- ACTUALIZAR CON FUNCIONES
UPDATE alumno set email = CONCAT(nombre, '@correo.com') WHERE id != 1;

---ELIMINAR REGISTROS (DELETE)
DELETE FROM alumno WHERE id = 10;