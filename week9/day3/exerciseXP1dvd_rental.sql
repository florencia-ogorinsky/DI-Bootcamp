--Exercise 1: DVD Rental

--1 Get a list of all the languages, from the language table.

select distinct name as list_of_names from 

--2 Get a list of all films joined with their languages – select the following details : film title, description, and language name.

select * from language

select * from film

select f.title, f.description, l.name
from film as f
join language as l on f.language_id=l.language_id

--3 Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
select f.title, f.description, l.name
from language as l
left join film as f on f.language_id = l.language_id

--4 Create a new table called new_film with the following columns : id, name. Add some new films to the table.

create table new_film (id serial primary key, name varchar(100) not null);

insert into new_film(name)
values('El secreto de sus ojos'), ('El amor menos pensado'),('Truman');

select * from new_film


--Create a new table called customer_review, which will contain film reviews that customers will make.
--Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.

create table customer_review (
    review_id serial primary key,
    film_id integer not null,
    language_id smallint not null,
    title varchar(255) not null,
    score smallint not null check (score >= 1 and score <= 10),
    review_text text,
    last_update timestamp without time zone default current_timestamp,
    constraint fk_film_review_film
        foreign key (film_id)
        references new_film(id)
        on delete cascade,
    constraint fk_customer_review_language
        foreign key (language_id)
        references language(language_id)
);

select * from customer_review


--Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

insert into customer_review (film_id, language_id, title, score, review_text)
values (1, 1, 'Great Movie!', 9, 'This film was fantastic. The acting and visuals were all incredible.'),
       (2, 2, 'Un poco decepcionante', 6, 'La película estuvo bien, pero esperaba más basándome en las críticas.');

select * from customer_review;


--Delete a film that has a review from the new_film table, what happens to the customer_review table?
--it will be deleted also because of the 'on delete cascade'

delete from new_film where id = 1;

select * from customer_review;
