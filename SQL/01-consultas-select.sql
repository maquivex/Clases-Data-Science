-- CONSULTAS SELECT
select * from empleados;
select nombre,pais from empleados;
select * from empleados order by nombre;
select * from empleados order by salario desc;

-- filtros
select * from empleados where pais = 'Peru';
select * from empleados where salario > 5000;
select * from empleados where salario > 5000 and pais = 'Peru';
select * from empleados where salario BETWEEN 1000 AND 3000;