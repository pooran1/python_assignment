
-- # table: employees
-- Select first 10 records from the table.
SELECT * FROM employees
LIMIT 10;

-- Display the names (first_name, last_name) using alias name "First Name", "Last Name".
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;

-- Get unique department ID list.
SELECT DISTINCT department_id
FROM employees;

-- Get all employee details from the employee table ordered by first name, descending.
SELECT * FROM employees
ORDER BY first_name DESC;

-- Display fullname and salary.
SELECT CONCAT(first_name, ' ', last_name) AS fullname, salary
FROM employees;

-- Display all employees' salary-wise from lowest to highest.
SELECT * FROM employees
ORDER BY salary ASC;

-- How much money the company is spending on employees' salary.
SELECT SUM(salary) AS total_salary_expenditure
FROM employees;

-- Show min, max, and avg salary of company staff.
SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary, AVG(salary) AS avg_salary
FROM employees;

-- Show employee name, their salary, and the avg salary of all staff.
SELECT CONCAT(first_name, ' ', last_name) AS fullname, salary, 
       (SELECT AVG(salary) FROM employees) AS avg_salary
FROM employees;

-- How many employees does the company have, display the count.
SELECT COUNT(*) AS employee_count
FROM employees;

-- Show the number of employees in the company and the avg salary of all staff.
SELECT COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM employees;

-- Get the number of jobs available in the employees table.
SELECT COUNT(DISTINCT job_id) AS job_count
FROM employees;

-- Get all first names from employees table in upper case.
SELECT UPPER(first_name) AS first_name_upper
FROM employees;

-- Get first name from employees table after removing white spaces from both sides.
SELECT TRIM(first_name) AS trimmed_first_name
FROM employees;

-- Get monthly salary (round 2 decimal places) of each and every employee.
-- Note: Assume the salary field provides the 'annual salary' information.
SELECT first_name, last_name, 
       ROUND(salary / 12, 2) AS monthly_salary
FROM employees;

-- Find the 3rd highest paid employee.
-- Note: The query should return 1 row only.
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;

-- Display the fullname (first_name, last_name) and salary for all employees 
-- whose salary is in the range $10,000 through $15,000.
SELECT CONCAT(first_name, ' ', last_name) AS fullname, salary
FROM employees
WHERE salary BETWEEN 10000 AND 15000;

-- Display the fullname (first_name, last_name) and department ID of all employees 
-- in departments 30 or 100, sorted by department.
SELECT CONCAT(first_name, ' ', last_name) AS fullname, department_id
FROM employees
WHERE department_id IN (30, 100)
ORDER BY department_id ASC;

-- Display the fullname (first_name, last_name) and salary for all employees 
-- whose salary is in the range $10,000 through $15,000 and are in department 30 or 100.
SELECT CONCAT(first_name, ' ', last_name) AS fullname, salary
FROM employees
WHERE salary BETWEEN 10000 AND 15000
AND department_id IN (30, 100);

-- Display the fullname (first_name, last_name) and hire date for all employees 
-- who were hired in 1987.
SELECT CONCAT(first_name, ' ', last_name) AS fullname, hire_date
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) = 1987;

-- Display the last name, job, and salary for all employees whose job is that of a 
-- Programmer or a Shipping Clerk, and whose salary is not equal to $4,500, $10,000, or $15,000.
SELECT last_name, job_id, salary
FROM employees
WHERE job_id IN ('PROGRAMMER', 'SHIPPING_CLERK')
AND salary NOT IN (4500, 10000, 15000);

-- Select all records from employees where last name is in 'BLAKE', 'SCOTT', 'KING', and 'FORD'.
SELECT * FROM employees
WHERE last_name IN ('BLAKE', 'SCOTT', 'KING', 'FORD');


-- ## Datetime
-- Get the first name and hire date from employees table where hire date is between '1987-06-01' and '1987-07-30'.
SELECT first_name, hire_date
FROM employees
WHERE hire_date BETWEEN '1987-06-01' AND '1987-07-30';

-- Get the first name of employees who joined in 1987.
SELECT first_name
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) = 1987;

-- Get the first name of employees who joined in 1987 and 1989.
SELECT first_name
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) IN (1987, 1989);

-- Get the first name of employees who joined between 1987 and 2000.
SELECT first_name
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) BETWEEN 1987 AND 2000;

-- Get the firstname and lastname of employees who joined in the month of June.
SELECT first_name, last_name
FROM employees
WHERE EXTRACT(MONTH FROM hire_date) = 6;

-- Find employees hired within the last 90 days.
SELECT * FROM employees
WHERE hire_date >= CURRENT_DATE - INTERVAL '90' DAY;

-- List employees hired before the year 2010.
SELECT * FROM employees
WHERE EXTRACT(YEAR FROM hire_date) < 2010;




-- Fetch the name of jobs the company has using the table employees.
SELECT DISTINCT job_id
FROM employees;

-- Show how much the company spends on salaries and also display the count. Use table employees.
SELECT SUM(salary) AS total_salary_expenditure, COUNT(*) AS employee_count
FROM employees;

-- Display the minimum salary that a company is giving and also display the count. Use table employees.
SELECT MIN(salary) AS min_salary, COUNT(*) AS employee_count
FROM employees;

-- Display the maximum salary that a company is giving and also display the count. Use table employees.
SELECT MAX(salary) AS max_salary, COUNT(*) AS employee_count
FROM employees;

-- Get the highest, lowest, sum, and average salary among all employees.
SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary, 
       SUM(salary) AS total_salary, AVG(salary) AS avg_salary
FROM employees;

-- Display the maximum salary that a company is giving in the department IT_PROG.
SELECT MAX(salary) AS max_salary_in_it_prog
FROM employees
WHERE job_id = 'IT_PROG';

