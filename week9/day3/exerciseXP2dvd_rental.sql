--Use UPDATE to change the language of some films. Make sure that you use valid languages.

update film
set language_id = (select language_id from language where name = 'Italian')
where title in ('Aisport Pollock', 'Agent Truman');


--Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

SELECT 
    conname AS constraint_name,
    conrelid::regclass AS table_name,
    a.attname AS column_name,
    c.confrelid::regclass AS foreign_table_name,
    d.attname AS foreign_column_name
FROM 
    pg_constraint AS c
    JOIN pg_attribute AS a 
        ON a.attnum = ANY(c.conkey)
    JOIN pg_attribute AS d 
        ON d.attnum = ANY(c.confkey)
WHERE 
    c.conrelid = 'customer'::regclass;

select * from customer
--the foreign key is address_id from customer that is related to address table to column address_id
--To insert values into the customer table, must ensure that the address_id value in Insert already exists in the address table.

--We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
drop table customer_review;
--we need to check how it was related to new_film table cause we had foreign key there

--Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
select count(*) as outstanding_rentals 
from rental
where return_date is null;
--183

--Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
select f.title, f.replacement_cost
from rental r
join inventory i on r.inventory_id = i.inventory_id
join film f on i.film_id = f.film_id
where r.return_date is null
order by f.replacement_cost desc
limit 30;

--Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
--The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select
    f.title,
    f.description
from
    film f
join
    film_actor fa on f.film_id = fa.film_id
join
    actor a on fa.actor_id = a.actor_id
where
    f.description like '%Sumo Wrestler%'
    and a.first_name = 'Penelope'
    and a.last_name = 'Monroe';


--The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT
    f.title,
    f.length,
    f.rating
FROM
    film f
JOIN
    film_category fc ON f.film_id = fc.film_id
JOIN
    category c ON fc.category_id = c.category_id
WHERE
    f.length < 60
    AND f.rating = 'R'
    AND c.name = 'Documentary';

--The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT
    f.title
FROM
    customer c
JOIN
    rental r ON c.customer_id = r.customer_id
JOIN
    payment p ON r.rental_id = p.rental_id
JOIN
    inventory i ON r.inventory_id = i.inventory_id
JOIN
    film f ON i.film_id = f.film_id
WHERE
    c.first_name = 'Matthew'
    AND c.last_name = 'Mahan'
    AND p.amount > 4.00
    AND r.return_date >= '2005-07-28'
    AND r.return_date <= '2005-08-01';

--Sugar Wonka

--The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT
    f.title,
    f.description,
    f.replacement_cost
FROM
    customer c
JOIN
    rental r ON c.customer_id = r.customer_id
JOIN
    inventory i ON r.inventory_id = i.inventory_id
JOIN
    film f ON i.film_id = f.film_id
WHERE
    c.first_name = 'Matthew'
    AND c.last_name = 'Mahan'
    AND (f.title LIKE '%Boat%' OR f.description LIKE '%Boat%')
ORDER BY
    f.replacement_cost DESC;


