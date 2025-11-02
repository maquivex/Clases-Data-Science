-- AGRUPACIONES
-- 1 CONTAR
select count(*) from empleados;
select count(*) from empleados where salario > 5000;

-- 2 MAXIMOS Y MINIMOS
select max(salario) from empleados;
select min(salario) from empleados;
select avg(salario) from empleados;

select max(salario),min(salario),avg(salario) from empleados;

select DISTINCT pais from empleados;

-- SELECCIONAR EL TOTAL DE EMPLEADOS POR PAIS
select pais,count(*) from empleados
group by pais
order by count(*) desc;

select pais,area,max(salario),min(salario),avg(salario) from empleados
where salario > 5000
group by pais,area

-- subconsultas
-- consultas todos los empleados cuyo salario es mayor al promedio
select avg(salario) from empleados;
select nombre,salario from empleados
where salario > (select avg(salario) from empleados);

select pais,count(*) as total,(select avg(salario) from empleados) as salario_promedio
from empleados
group by pais order by count(*) desc