create database cadastro;

use cadastro;

create table gafanhotos (
id int not null auto_increment,
nome varchar(30) not null,
nascimento date,
sexo enum('M', 'F'),
peso decimal(5,2),
altura decimal(3,2),
nacionalidade varchar(20) default 'Brasil',
primary key (id)
) default charset = utf8;

insert into gafanhotos values
('1', 'Cláudio', '1975-4-22', 'M', '99.0', '2.15', 'Brasil'),
('2', 'Pedro', '1999-12-3', 'M', '87', '2', default),
('3', 'Janaína', '1987-11-12', 'F', '75.4', '1.66', 'EUA');

select * from gafanhotos;

create table if not exists cursos (
nome varchar(30) not null unique,
descricao text,
carga int unsigned,
totaulas int unsigned,
ano year default '2016'
) default charset=utf8;

desc cursos;

desc gafanhotos;

alter table gafanhotos
add column cursopreferido int;

alter table gafanhotos
add foreign key (cursopreferido)
references cursos(idcurso);

select * from gafanhotos;
select * from cursos;

update gafanhotos set cursopreferido = '6' where id = '1';

alter table cursos
add column idcurso int first;

alter table cursos add primary key (idcurso);

select * from cursos
order by nome desc;

select * from cursos
order by nome asc;

select ano, nome, carga from cursos
order by ano, nome;

select nome, carga, ano from cursos
where ano <= '2016'
order by nome;

select nome, ano from cursos
where ano between 2014 and 2016
order by ano desc, nome;

select nome, descricao, ano from cursos
where ano in (2014, 2016)
order by ano;

select * from cursos
where carga > 35 or totaulas < 30
order by nome;

select * from cursos
where nome like 'p%';

select * from cursos
where nome like '%a';

select * from cursos
where nome like '%a%';

select * from cursos
where nome like 'ph%p';

select * from cursos
where nome like 'ph%p%';

select * from cursos
where nome like 'ph%p_';

select distinct nacionalidade from gafanhotos
order by nacionalidade;

select count(*) from cursos;

select count(*) from cursos where carga > 40;

select max(totaulas) from cursos where ano = '2016';

select min(totaulas) from cursos where ano = '2016';

select sum(carga) from cursos;

select avg(totaulas) from cursos where ano = '2016';

select distinct carga from cursos
order by carga desc;

select carga from cursos
group by carga;

select carga, count(nome) from cursos
group by carga;

select totaulas, count(*) from cursos
group by totaulas
order by totaulas;

select carga, count(nome) from cursos where totaulas = 30
group by carga;

select ano, count(*) from cursos
group by ano
having count(ano) >= 5
order by count(*) desc;

select avg(carga) from cursos;

select carga, count(*) from cursos
where ano > 2015
group by carga
having carga > (select avg(carga) from cursos);

insert into cursos values
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algoritmos', 'Lógica de Programação', '20', '15', '2014'),
('3', 'Pothoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4', 'PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introdução à Linguagem Java', '10', '29', '2000'),
('6', 'MySQL', 'Banco de Dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso completo de Word', '40', '30', '2018'),
('8', 'Sapateado', 'Danças Rítmicas', '40', '30', '2018'),
('9', 'Cozinha Árabe', 'Aprenda a fazer Kibe', '40', '30', '2018'),
('10', 'YouTuber', 'Gerar polêmica e ganhar inscritos', '5', '2', '2018');

select nome, cursopreferido from gafanhotos;

select nome, ano from cursos;

select g.nome, c.nome, c.ano
from gafanhotos as g inner join cursos as c
on c.idcurso = g.cursopreferido
order by g.nome;

select g.nome, c.nome, c.ano
from gafanhotos as g left join cursos as c
on c.idcurso = g.cursopreferido
order by g.nome;

create table gafanhoto_assiste_curso (
id int not null auto_increment,
data date,
idgafanhoto int,
idcurso int,
primary key (id),
foreign key (idgafanhoto) references gafanhotos(id),
foreign key (idcurso) references cursos(idcurso)
) default charset = utf8;

insert into gafanhoto_assiste_curso values
(default, '2014-03-01', '1', '2');

select * from gafanhoto_assiste_curso;

select g.nome, c.nome from gafanhotos g
join gafanhoto_assiste_curso a
on g.id = a.idgafanhoto
join cursos c
on c.idcurso = a.idcurso
order by g.nome;

select * from departamento;
select * from empregado;

create table empregado (
id int not null auto_increment,
salario int,
departamento_id int,
primary key (id),
foreign key (departamento_id) references departamento(id)
) default charset = utf8;

create table departamento (
id int not null auto_increment,
nome varchar(30) not null,
primary key (id)
) default charset = utf8;

insert into empregado values
(default, '1000', '2'),
(default, '1250', '4'),
(default, '2500', '1'),
(default, '3900', '3');

insert into departamento values
(default, 'Informática'),
(default, 'Finanças'),
(default, 'Pessoal'),
(default, 'Pagamento'),
(default, 'Administração');

SELECT departamento.nome
FROM departamento, empregado
WHERE departamento.id = empregado.departamento_id
AND empregado.salario > 2500;

create table empregado (
id int not null auto_increment,
nome varchar(30) not null,
idade int,
primary key (id)
) default charset = utf8;

create table pagamento (
empregado_id int not null auto_increment,
data date,
valor int,
foreign key (empregado_id) references empregado(id)
) default charset = utf8;

insert into empregado values
(default, 'João', '20'),
(default, 'Maria', '30'),
(default, 'José', '22'),
(default, 'Joaquim', '26'),
(default, 'Manoel', '21');

insert into pagamento values
('1', '02-07-08', '1000'),
('2', '02-07-08', '2000'),
('3', '02-07-08', '1400'),
('4', '02-07-08', '1200'),
('5', '02-07-08', '5000');

SELECT count(*)
FROM empregado, pagamento
WHERE empregado.id = pagamento.empregado_id
AND empregado.idade < 25 AND pagamento.valor > 1500;

select * from pagamento;
select * from empregado;

alter table empregado drop nome;