-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";

CREATE DATABASE "Hollywood"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


create table actors(
	actor_id serial primary key,
	first_name varchar(50) not null,
	last_name varchar (100) not null, 
	age date not null,
	number_oscars smallint not null
	)


insert into actors(first_name, last_name, age, number_oscars)
values ('Matt','Damon','08/10/1970',5),
		('George','Clooney','06/05/1961',2);

select * from actors;


select * 
from actors 
where first_name='Matt';

select * 
from actors 
where last_name like '%mon'

select * 
from actors 
where last_name ilike 'da%'  --case insensitive

insert into actors(first_name, last_name, age, number_oscars)
values ('Angelina','Jolie','06/04/1975',5),
		('Jennifer','Aniston','11/02/1961',2);

--1. Count how many actors are in the table.

select count (actor_id) as "number of actors"
from actors;

--2. Try to add a new actor with some blank fields. What do you think the outcome will be ?

insert into actors (first_name, last_name, age, number_oscars)
values ('Florencia', null, null, 0)

--we set the fields to be not null so we get error ERROR:  null value in column "last_name" of relation "actors" violates not-null constraint

