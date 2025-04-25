--🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis
-- Create a temporary table by joining all tables using LEFT JOIN
-- Create a temporary table by joining all tables using LEFT JOIN
-- Create a temporary table by joining all tables using LEFT JOIN
-- Create a temporary table by joining all tables using LEFT JOIN
-- Create a temporary table by joining all tables using LEFT JOIN


-- Elimina la tabla emp_dataset si ya existe
DROP TABLE IF EXISTS emp_dataset;

-- Crea emp_dataset combinando todas las tablas
CREATE TABLE emp_dataset AS
SELECT *
FROM salaries
LEFT JOIN companies ON salaries.comp_name = companies.company_name
LEFT JOIN functions ON salaries.func_code = functions.function_code
LEFT JOIN employees ON salaries.employee_id = employees.employee_code_emp;

-- Elimina df_employee si ya existe
DROP TABLE IF EXISTS df_employee;

-- Crea df_employee con los campos limpios
CREATE TABLE df_employee AS
SELECT 
    employee_id || CAST(date AS TEXT) AS id,
    CAST(date AS TEXT) AS month_year,
    employee_id, 
    employee_name, 
    "GEN(M_F)" AS gender,
    age,
    salary,
    function_group, 
    company_name, 
    company_city, 
    company_state, 
    company_type, 
    const_site_category
FROM emp_dataset;



select * from df_employee;



--🌟 Exercise 2: Cleaning Data for Consistency and Quality

--1. run the following SQLite request and observe your new table.
SELECT * FROM df_employee;


--2. Remove all unwanted spaces from all text columns using TRIM

UPDATE df_employee
SET		id = TRIM(id),
		employee_id	= TRIM(employee_id),
		employee_name = TRIM(employee_name),
		gender = TRIM(gender),
		function_group = TRIM(function_group),
		company_name = TRIM(company_name),
		company_city = TRIM(company_city),
		company_state = TRIM(company_state),
		company_type = TRIM(company_type),
		const_site_category = TRIM(const_site_category)


--3. Check for NULL values and empty values.

SELECT *
FROM df_employee
WHERE id IS NULL OR id = ''
   OR month_year IS NULL OR month_year = ''
   OR employee_id IS NULL OR employee_id = ''
   OR employee_name IS NULL OR employee_name = ''
   OR gender IS NULL OR gender = ''
   OR function_group IS NULL OR function_group = ''
   OR company_name IS NULL OR company_name = ''
   OR company_city IS NULL OR company_city = ''
   OR company_state IS NULL OR company_state = ''
   OR company_type IS NULL OR company_type = ''
   OR const_site_category IS NULL OR const_site_category = '';
   
   

--4. Delete rows of the detected missing values.
DELETE FROM df_employee
WHERE id IS NULL OR id = ''
   OR month_year IS NULL OR month_year = ''
   OR employee_id IS NULL OR employee_id = ''
   OR employee_name IS NULL OR employee_name = ''
   OR gender IS NULL OR gender = ''
   OR function_group IS NULL OR function_group = ''
   OR company_name IS NULL OR company_name = ''
   OR company_city IS NULL OR company_city = ''
   OR company_state IS NULL OR company_state = ''
   OR company_type IS NULL OR company_type = ''
   OR const_site_category IS NULL OR const_site_category = '';

select * from df_employee

--🌟 Exercise 3 : Calculating Current Employee Counts by Company
--How many employees do the companies have today?

SELECT COUNT(DISTINCT employee_id) AS employee_count 
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee);



--Group them by company

SELECT company_name, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY company_name
ORDER BY employee_count DESC;



--🌟 Exercise 4 : Analyzing Employee Distribution by City and Over Time
--What is the total number of employees each city? Add a percentage column
SELECT company_city, 
       COUNT(employee_id) AS employee_count,
       COUNT(employee_id) * 100.0 / (SELECT COUNT(*) FROM df_employee WHERE month_year = (SELECT MAX(month_year) FROM df_employee)) AS percentage
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY company_city
ORDER BY employee_count DESC;


--What is the total number of employees each month?

SELECT month_year, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY month_year
ORDER BY month_year ASC;


--What is the average number of employees each month?
SELECT (COUNT(employee_id) * 1.0 / COUNT(DISTINCT month_year)) AS avg_employees_per_month
FROM df_employee;


--🌟 Exercise 5 : Analyzing Employment Trends and Salary Metrics
--What is the minimum and maximum number of employees throughout all the months? In which months were they?

--Minimum:
SELECT month_year, COUNT(employee_id) AS count_employees_per_month
FROM df_employee
GROUP BY month_year
ORDER BY count_employees_per_month ASC
LIMIT 1;

--Maximum:
SELECT month_year, COUNT(employee_id) AS count_employees_per_month
FROM df_employee
GROUP BY month_year
ORDER BY count_employees_per_month DESC
LIMIT 1;

--What is the monthly average number of employees by function group?

SELECT function_group, 
       (COUNT(employee_id) * 1.0 / COUNT(DISTINCT month_year)) AS avg_employees_per_month
FROM df_employee
GROUP BY function_group
ORDER BY avg_employees_per_month DESC;

--What is the annual average salary?

SELECT substr(month_year, 1, 4) AS year, 
       ROUND(AVG(salary), 2) AS average_salary
FROM df_employee
GROUP BY substr(month_year, 1, 4)
ORDER BY year;





