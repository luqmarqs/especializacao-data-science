
--quest�o 1
CREATE TABLE ALUNOS (
 id_aluno int IDENTITY(1,1) PRIMARY KEY,
 nome_aluno varchar(50),
 cpf int UNIQUE,
  data_cadastro datetime
)

--quest�o 2
CREATE TABLE DISCIPLINAS (
  id_disciplina int identity(1,1) PRIMARY KEY,
  nome_disciplina varchar(25),
  nome_professor varchar(50),
  data_cadastro datetime
)

--quest�o 3
CREATE TABLE ALUNODISCIPLINA(
  id int IDENTITY(1,1) PRIMARY KEY,
  id_aluno int not null,
  id_disciplina int not null,
  data_cadastro datetime,
  foreign key (id_aluno) references ALUNOS(id_aluno),
  foreign key (id_disciplina) references DISCIPLINAS(id_disciplina)
)

--quest�o 4
insert into ALUNOS values('Jo�o da Silva', 2712397, GETDATE());
insert into ALUNOS values('Jos� de Almeida', 64142104, GETDATE());
insert into ALUNOS values('Maria dos Anjos', 931158299, GETDATE());
insert into ALUNOS values('Cleber Antonio', 656753300, GETDATE());
insert into ALUNOS values('Aline Miranda', 78488282, GETDATE());
insert into ALUNOS values('Clara Saraiva', 52749569, GETDATE());
insert into ALUNOS values('Carlos Eduardo', 12456809, GETDATE());
insert into ALUNOS values('Jo�o Pedro', 75463180, GETDATE());

insert into DISCIPLINAS values ('Matem�tica', 'Antonio Pedro', GETDATE());
insert into DISCIPLINAS values ('Portugu�s', 'Michel Lopes', GETDATE());
insert into DISCIPLINAS values ('Qu�mica', 'Angela Araujo', GETDATE());
insert into DISCIPLINAS values ('Hist�ria', 'Bruno Carvalho', GETDATE());

insert into ALUNODISCIPLINA values (17, 1, GETDATE());
insert into ALUNODISCIPLINA values (23, 1, GETDATE());
insert into ALUNODISCIPLINA values (30, 2, GETDATE());
insert into ALUNODISCIPLINA values (32, 3, GETDATE());
insert into ALUNODISCIPLINA values (34, 4, GETDATE());
insert into ALUNODISCIPLINA values (23, 2, GETDATE());

--quest�o 5
select nome_aluno from ALUNOS
inner join ALUNODISCIPLINA on ALUNOS.id_aluno = ALUNODISCIPLINA.id_aluno
inner join DISCIPLINAS on ALUNODISCIPLINA.id_disciplina = DISCIPLINAS.id_disciplina
where DISCIPLINAS.id_disciplina = 1

--quest�o 6
delete from ALUNOS where id_aluno not in (select id_aluno from ALUNODISCIPLINA)


select * from ALUNOS

select * from DISCIPLINAS

select * from ALUNODISCIPLINA


