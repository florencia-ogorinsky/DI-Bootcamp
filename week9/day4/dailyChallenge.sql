--🌟 Exercise 1: Detailed Medal Analysis

--Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter 
--Olympics. Create a temporary table to store these competitors and their medal counts for each season, 
--and then display the contents of this table.


CREATE TEMP TABLE CompetitorsBothSeasons AS
SELECT
    p.id AS person_id,
    p.full_name,
    SUM(CASE WHEN g.season = 'Summer' AND ce.medal_id IS NOT NULL THEN 1 ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN g.season = 'Winter' AND ce.medal_id IS NOT NULL THEN 1 ELSE 0 END) AS winter_medals
FROM
    person p
JOIN
    games_competitor gc ON p.id = gc.person_id
JOIN
    games g ON gc.games_id = g.id
JOIN
    competitor_event ce ON gc.id = ce.competitor_id
WHERE
    ce.medal_id IS NOT NULL
GROUP BY
    p.id, p.full_name
HAVING
    SUM(CASE WHEN g.season = 'Summer' AND ce.medal_id IS NOT NULL THEN 1 ELSE 0 END) > 0 AND
    SUM(CASE WHEN g.season = 'Winter' AND ce.medal_id IS NOT NULL THEN 1 ELSE 0 END) > 0;


SELECT * FROM CompetitorsBothSeasons;



--Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, 
--and then use a subquery to identify the top 3 competitors with the highest total number of medals across 
--all sports. Display the contents of this table.


-- Create a temporary table for competitors winning medals in exactly two sports
CREATE TEMP TABLE CompetitorsTwoSports AS
SELECT
    p.id AS person_id,
    p.full_name,
    COUNT(DISTINCT ev.sport_id) AS num_sports_with_medal
FROM
    person p
JOIN
    games_competitor gc ON p.id = gc.person_id
JOIN
    competitor_event ce ON gc.id = ce.competitor_id
JOIN
    event ev ON ce.event_id = ev.id
WHERE
    ce.medal_id IS NOT NULL
GROUP BY
    p.id, p.full_name
HAVING
    COUNT(DISTINCT ev.sport_id) = 2;


SELECT * FROM CompetitorsTwoSports;

-- top 3 competitors from the temporary table with highest total medals
SELECT
    cts.full_name,
    (SELECT COUNT(*)
     FROM competitor_event ce
     JOIN games_competitor gc ON ce.competitor_id = gc.id
     WHERE gc.person_id = cts.person_id AND ce.medal_id IS NOT NULL) AS total_medals
FROM
    CompetitorsTwoSports cts
ORDER BY
    total_medals DESC
LIMIT 3;


--🌟 Exercise 2: Region and Competitor Performance
--Task 1: Retrieve the regions that have competitors who have won the highest number of 
--medals in a single Olympic event. Use a subquery to determine the event with the highest number 
--of medals for each competitor, and then display the top 5 regions with the highest total medals.

WITH CompetitorMaxMedals AS (
    SELECT
        gc.person_id,
        COUNT(*) AS max_medals_single_event
    FROM
        games_competitor gc
    JOIN
        competitor_event ce ON gc.id = ce.competitor_id
    WHERE
        ce.medal_id IS NOT NULL
    GROUP BY
        gc.person_id, ce.event_id
),
RegionMaxMedals AS (
    SELECT
        pr.region_id,
        SUM(cmm.max_medals_single_event) AS total_max_medals
    FROM
        CompetitorMaxMedals cmm
    JOIN
        person_region pr ON cmm.person_id = pr.person_id
    GROUP BY
        pr.region_id
)
SELECT
    nr.region_name,
    rmm.total_max_medals
FROM
    RegionMaxMedals rmm
JOIN
    noc_region nr ON rmm.region_id = nr.id
ORDER BY
    rmm.total_max_medals DESC
LIMIT 5;



--Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals. Retrieve and display the contents of this table, including their full names and the number of games they participated in.

DROP TABLE IF EXISTS NoMedalFrequentCompetitors;
CREATE TEMP TABLE NoMedalFrequentCompetitors AS
SELECT
    p.id AS person_id,
    p.full_name,
    COUNT(DISTINCT g.id) AS num_games_participated
FROM
    person p
JOIN
    games_competitor gc ON p.id = gc.person_id
JOIN
    games g ON gc.games_id = g.id
WHERE
    NOT EXISTS (
        SELECT 1
        FROM competitor_event ce
        WHERE ce.competitor_id = gc.id AND ce.medal_id IS NOT NULL
    )
GROUP BY
    p.id, p.full_name
HAVING
    COUNT(DISTINCT g.id) > 3;

SELECT * FROM NoMedalFrequentCompetitors;