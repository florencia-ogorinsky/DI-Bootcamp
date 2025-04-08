CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

--it creates 1 table called FirstTab and 2 columns, id and name

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

-- is adding values to the columns that we just created

SELECT * FROM FirstTab

--is showing the table


CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)

--creating second table called SecondTab with only 1 column called id and inserting 2 values to it, 5 and null

SELECT * FROM SecondTab

--displaying the table


--Q1. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
--0
--where ft.id not in (NULL) means is ft.id different from all values from null? 
--then is 5 different from null? unknown. 6 != 0? unknown. Null is always considered unknown so
--So the count will be 0 because we cant supposed they are different


--Q2. What will be the OUTPUT of the following statement?
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- 2 because there are 2 ids that are different from 5 (not 3 because 1 is unknown, is not true)


--Q3. What will be the OUTPUT of the following statement?
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

--0 because some of theme are unknown so we cant say they are not present in the other tab

--Q4. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

--2 because the where select rows where id is not in 5, meaning 6 and 7