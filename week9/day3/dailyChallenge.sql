--Part I

--Create 2 tables : Customer and Customer profile. They have a One to One relationship.

--A customer can have only one profile, and a profile belongs to only one customer
--The Customer table should have the columns : id, first_name, last_name NOT NULL
--The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)

create table customer (
    id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null
);

create table customer_profile (
    id serial primary key,
    isloggedin boolean default false,
    customer_id integer unique references customer(id)
);

--Insert those customers
--John, Doe
--Jerome, Lalu
--Lea, Rive

insert into customer (first_name, last_name)
values ('John', 'Doe'),
       ('Jerome', 'Lalu'),
       ('Lea', 'Rive');


--Insert those customer profiles, use subqueries
--John is loggedIn
--Jerome is not logged in

insert into customer_profile (customer_id, isloggedin)
values ((select id from customer where first_name = 'John'), true),
       ((select id from customer where first_name = 'Jerome'), false);

--Use the relevant types of Joins to display:
--The first_name of the LoggedIn customers

select c.first_name
from customer c
inner join customer_profile cp on c.id = cp.customer_id
where cp.isloggedin = true;

--All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
select c.first_name, cp.isloggedin
from customer c
left join customer_profile cp on c.id = cp.customer_id;

--The number of customers that are not LoggedIn
select count(*)
from customer c
left join customer_profile cp on c.id = cp.customer_id
where cp.isloggedin = false or cp.isloggedin is null;

--Part II:

--Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
create table book (
    book_id serial primary key,
    title varchar(300) not null,
    author varchar(300) not null
);

--Insert those books :
--Alice In Wonderland, Lewis Carroll
--Harry Potter, J.K Rowling
--To kill a mockingbird, Harper Lee

insert into book (title, author)
values ('Alice In Wonderland', 'Lewis Carroll'),
       ('Harry Potter', 'J.K Rowling'),
       ('To kill a mockingbird', 'Harper Lee');

--Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);
create table student (
    student_id serial primary key,
    name varchar(300) not null unique,
    age integer check (age <= 15)
);

--Insert those students:
--John, 12
--Lera, 11
--Patrick, 10
--Bob, 14

insert into student (name, age)
values ('John', 12),
       ('Lera', 11),
       ('Patrick', 10),
       ('Bob', 14);

-- Create a table named Library, with the columns:
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables: A student can borrow many books, and a book can be borrowed by many children.
-- book_fk_id is a Foreign Key representing the column book_id from the Book table.
-- student_fk_id is a Foreign Key representing the column student_id from the Student table.
-- The pair of Foreign Keys is the Primary Key of the Junction Table.


create table library (
    book_fk_id integer references book(book_id) on delete cascade on update cascade,
    student_fk_id integer references student(student_id) on delete cascade on update cascade,
    borrowed_date date,
    primary key (book_fk_id, student_fk_id)
);

-- Add 4 records in the junction table, use subqueries.
-- The student named John, borrowed the book Alice In Wonderland on the 15/02/2022.
-- The student named Bob, borrowed the book To Kill a Mockingbird on the 03/03/2021.
-- The student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021.
-- The student named Bob, borrowed the book Harry Potter on the 12/08/2021.
insert into library (student_fk_id, book_fk_id, borrowed_date)
values ((select student_id from student where name = 'John'), (select book_id from book where title = 'Alice In Wonderland'), '2022-02-15'),
       ((select student_id from student where name = 'Bob'), (select book_id from book where title = 'To kill a mockingbird'), '2021-03-03'),
       ((select student_id from student where name = 'Lera'), (select book_id from book where title = 'Alice In Wonderland'), '2021-05-23'),
       ((select student_id from student where name = 'Bob'), (select book_id from book where title = 'Harry Potter'), '2021-08-12');

-- Display the data
-- Select all the columns from the junction table
select * from library;

-- Select the name of the student and the title of the borrowed books
select s.name as student_name, b.title as book_title
from library l
join student s on l.student_fk_id = s.student_id
join book b on l.book_fk_id = b.book_id;

-- Select the average age of the children, that borrowed the book Alice in Wonderland
select avg(s.age)::integer as average_age
from library l
join student s on l.student_fk_id = s.student_id
join book b on l.book_fk_id = b.book_id
where b.title ='Alice In Wonderland';

-- Delete a student from the Student table, what happened in the junction table?

delete from student where name = 'John'; 

-- when a student is deleted from the student, related records in the library table are also deleted
-- because of "on delete cascade"

select * from library 
