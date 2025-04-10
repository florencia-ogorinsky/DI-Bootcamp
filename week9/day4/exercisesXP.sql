--🌟 Exercise 1: Complex Subquery Analysis

--Task 1: Find the average age of competitors who have won at least one medal, 
--grouped by the type of medal they won. Use a correlated subquery to achieve this.


CREATE INDEX IF NOT EXISTS idx_medal_id ON competitor_event(medal_id);
CREATE INDEX IF NOT EXISTS idx_competitor_id ON competitor_event(competitor_id);
CREATE INDEX IF NOT EXISTS idx_person_id ON games_competitor(person_id);


SELECT m.medal_name,
  (
    SELECT AVG(g.age)
    FROM games_competitor AS g
    WHERE g.person_id IN (
      SELECT ce.competitor_id
      FROM competitor_event AS ce
      WHERE ce.medal_id = m.id
    )
  ) AS avg_age
FROM medal AS m
WHERE m.id IS NOT NULL
LIMIT 10;  



--Task 2: Identify the top 5 regions with the highest number of unique competitors
--who have participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.

SELECT nr.region_name, COUNT(*) AS num_competitors
FROM (
  SELECT DISTINCT g.person_id
  FROM games_competitor AS g
  WHERE g.person_id IN (
    SELECT ce.competitor_id
    FROM competitor_event AS ce
    GROUP BY ce.competitor_id
    HAVING COUNT(DISTINCT ce.event_id) > 3
  )
) AS qualified
JOIN person_region AS pr ON qualified.person_id = pr.person_id
JOIN noc_region AS nr ON pr.region_id = nr.id
GROUP BY nr.region_name
ORDER BY num_competitors DESC
LIMIT 5;

--Task 3: Create a temporary table to store the total number of medals won 
--by each competitor and filter to show only those who have won more than 2 medals. 
--Use subqueries to aggregate the data.


-- medals by competitor
CREATE TEMPORARY TABLE medal_count AS
SELECT competitor_id, COUNT(*) AS total_medals
FROM competitor_event
WHERE medal_id IS NOT NULL
GROUP BY competitor_id;

-- competitors more than 2 medals
SELECT competitor_id, total_medals
FROM (
  SELECT competitor_id, COUNT(*) AS total_medals
  FROM competitor_event
  WHERE medal_id IS NOT NULL
  GROUP BY competitor_id
) AS medal_count
WHERE total_medals > 2;

--Task 4: Use a subquery within a DELETE statement to remove records of competitors who 
--have not won any medals from a temporary table created for analysis.

DROP TABLE IF EXISTS medal_count;

CREATE TEMPORARY TABLE medal_count AS
SELECT competitor_id, COUNT(*) AS total_medals
FROM competitor_event
WHERE medal_id IS NOT NULL
GROUP BY competitor_id;


DELETE FROM medal_count
WHERE total_medals = 0;

SELECT * FROM medal_count;



--🌟 Exercise 2: Advanced Data Manipulation and Optimization

--Task 1: Update the heights of competitors based on the average height of competitors from the same region. 
--Use a correlated subquery within the UPDATE statement.

--to save original value in new column cause we will change the values:
ALTER TABLE person ADD COLUMN original_height REAL;

UPDATE person
SET original_height = height;

--change values for average: --we try only with 10 to see if it works. cause for everyone will take a lot of time
UPDATE person
SET height = (
    SELECT AVG(p2.height)
    FROM person AS p2
    JOIN person_region AS pr2 ON p2.id = pr2.person_id
    WHERE pr2.region_id = (
        SELECT pr1.region_id
        FROM person_region AS pr1
        WHERE pr1.person_id = person.id
    )
    AND p2.height > 0
)
WHERE height = 0
AND id IN (
    SELECT id
    FROM person
    WHERE height = 0
    LIMIT 10
);



--compare original with modified:
SELECT id, original_height, height
FROM person
WHERE height != original_height;




--Task 2: Insert new records into a temporary table for competitors who participated 
--in more than one event in the same games and list their total number of events participated. 
--Use nested subqueries for filtering.

CREATE TEMP TABLE many_events AS
SELECT gc.games_id, gc.person_id, COUNT(DISTINCT ce.event_id) AS nb_events
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
GROUP BY gc.games_id, gc.person_id
HAVING nb_events > 1;


select * from many_events;


--Task 3: Identify regions where the average number of medals won per competitor is greater than 
--the overall average. Use subqueries to calculate and compare averages.

SELECT r.region_name, AVG(medals.medal_count) AS avg_medals
FROM (
  SELECT pr.region_id, ce.competitor_id, COUNT(ce.medal_id) AS medal_count
  FROM competitor_event ce
  JOIN games_competitor gc ON gc.id = ce.competitor_id
  JOIN person_region pr ON pr.person_id = gc.person_id
  WHERE ce.medal_id IS NOT NULL
  GROUP BY pr.region_id, ce.competitor_id
) AS medals
JOIN noc_region r ON medals.region_id = r.id
GROUP BY r.region_name
HAVING AVG(medals.medal_count) > (
  SELECT AVG(m.total_medals)
  FROM (
    SELECT competitor_id, COUNT(medal_id) AS total_medals
    FROM competitor_event
    WHERE medal_id IS NOT NULL
    GROUP BY competitor_id
  ) AS m
);

--Task 4: Create a temporary table to track competitors’ participation across different seasons 
--and identify those who have participated in both Summer and Winter games.

-- temporary table
CREATE TEMP TABLE CompetitorSeasons AS
SELECT
    gc.person_id,
    g.season
FROM
    games_competitor gc
JOIN
    games g ON gc.games_id = g.id
GROUP BY
    gc.person_id,
    g.season;
    
    
SELECT * FROM CompetitorSeasons;


--competitors from summer and winter 
SELECT
    person_id
FROM
    CompetitorSeasons
WHERE
    season IN ('Summer', 'Winter')
GROUP BY
    person_id
HAVING
    COUNT(DISTINCT season) = 2;