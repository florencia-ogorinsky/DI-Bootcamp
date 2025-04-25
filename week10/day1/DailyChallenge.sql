--Daily Challenge: Cleaning and Transforming Employee Record Data with SQL


-- Create the employees table
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);

-- Insert 20 sample records 
INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');


--Identify and handle any missing value.
SELECT 
    COUNT(*) AS total_records,
    SUM(CASE WHEN employee_name IS NULL THEN 1 ELSE 0 END) AS missing_employee_name,
    SUM(CASE WHEN salary IS NULL THEN 1 ELSE 0 END) AS missing_salary,
    SUM(CASE WHEN hire_date IS NULL THEN 1 ELSE 0 END) AS missing_hire_date,
    SUM(CASE WHEN department IS NULL THEN 1 ELSE 0 END) AS missing_department
FROM employees;

UPDATE employees
SET department = 'Unknown'
WHERE department IS NULL;


--Check for and eliminate any duplicate rows in the dataset.
DELETE FROM employees
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM employees
    GROUP BY employee_id, employee_name, salary, hire_date, department
);

--Correct any structural issues, such as inconsistent naming conventions or formatting errors.

UPDATE employees
SET employee_name = 
    UPPER(SUBSTR(employee_name, 1, 1)) || LOWER(SUBSTR(employee_name, 2))
;

select * from employees

--Ensure all columns have appropriate data types (e.g. the hire_date column).


ALTER TABLE employees
ADD COLUMN hire_date_new DATE;

UPDATE employees
SET hire_date_new = STRFTIME('%Y-%m-%d', hire_date);

ALTER TABLE employees DROP COLUMN hire_date;
ALTER TABLE employees RENAME COLUMN hire_date_new TO hire_date;

select * from employees

--Detect and address any outliers that may skew the analysis.

SELECT employee_id, salary
FROM employees
WHERE salary < 5000 OR salary > 200000;


UPDATE employees
SET salary = (SELECT AVG(salary) FROM employees)
WHERE salary < 5000 OR salary > 200000;

--Standardize and normalize data where applicable to ensure consistency.

UPDATE employees
SET department = UPPER(department);

