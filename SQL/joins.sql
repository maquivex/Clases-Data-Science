-- A : ALUMNO
-- B : NOTAS
-- C : CURSO

-- LEFT JOIN entre ALUMNO y NOTAS para obtener todos los alumnos y sus notas (si las tienen)
select alumno.nombre,nota.nota
from alumno left join nota on nota.alumno_id=alumno.id;

insert into alumno(nro_documento,nombre) values('1001','Juan Perez');

-- RIGTH JOIN
insert into curso(nombre) values('Numpy y Pandas');

select curso.nombre,avg(nota.nota)
from nota RIGHT JOIN curso on nota.curso_id = curso.id
GROUP BY curso.nombre;

-- INNER JOIN
select curso.nombre,alumno.nombre,nota.nota 
FROM nota
inner join alumno on nota.alumno_id = alumno.id
inner join curso on nota.curso_id = curso.id
order by alumno.nombre;