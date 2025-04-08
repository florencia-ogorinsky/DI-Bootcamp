create table items (
	id serial primary key, 
	item varchar(100) not null,
	price int not null
);

insert into items(item, price)
values ('small desk', 100),
		('large desk', 300),
		('fan', 80);

create table customers (
	id serial primary key,
	first_name varchar(100) not null,
	last_name varchar(100) not null
);

insert into customers(first_name, last_name)
values ('Greg', 'Jones'),
		('Sandra', 'Jones'),
		('Scott', 'Scott'),
		('Trevor', 'Green'),
		('Melanie', 'Johnson');

select * from items;
select * from customers;

select * 
from items
where price>80;


select * 
from items
where price<300;


select *
from customers 
where last_name = 'Smith';


select *
from customers 
where last_name = 'Jones';

select *
from customers 
where first_name != 'Scott';


SELECT * FROM items; SELECT * FROM customers;
