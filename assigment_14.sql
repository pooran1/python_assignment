-- Group BY
-- Write a query to get the number of employees who has the same job title.
SELECT job_title, COUNT(*) AS employee_count
FROM employees
GROUP BY job_title;
--list down the lowest salary of the employee of every manager and also display the manager_id.
SELECT manager_id, MIN(salary) AS lowest_salary
FROM employees
GROUP BY manager_id;

--list down the total salaries of every deparment # NOTE: salary should be in ascending order

SELECT department_id, SUM(salary) AS total_salary
FROM employees
GROUP BY department_id
ORDER BY total_salary ASC;

--list down the average salaries of every department exluding IT Deparment
SELECT department_id, AVG(salary) AS average_salary
FROM employees
WHERE department_id NOT IN (
    SELECT department_id
    FROM departments
    WHERE department_name = 'IT'
)
GROUP BY department_id;


-- fetch the top 3 department who is taking the highest salary among all other deparment
SELECT department_id, SUM(salary) AS total_salary
FROM employees
GROUP BY department_id
ORDER BY total_salary DESC
LIMIT 3;


--# list down all the department (job_id) whose avg salary is more than overall avg salary of the whole company
WITH overall_avg_salary AS (
    SELECT AVG(salary) AS avg_salary
    FROM employees
)
SELECT job_id
FROM employees
GROUP BY job_id
HAVING AVG(salary) > (SELECT avg_salary FROM overall_avg_salary);

--# Write a query to get employee ID, last name, and date of first department (where he was working in, table name "job_history") of the employees.
SELECT jh.employee_id, e.last_name, MIN(jh.start_date) AS first_department_date
FROM job_history jh
JOIN employees e ON jh.employee_id = e.employee_id
GROUP BY jh.employee_id, e.last_name;

--# find the department that contains more than 10 employees
SELECT department_id
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 10;

--# Write a query to get the years in which more than 10 employees joined.

SELECT YEAR(hire_date) AS year_joined
FROM employees
GROUP BY YEAR(hire_date)
HAVING COUNT(*) > 10;


--Find the number of employees in each department.
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;

--Calculate the average salary for each job title.
SELECT job_id, AVG(salary) AS average_salary
FROM employees
GROUP BY job_id;

--List the total salary expenditure for each department.
SELECT department_id, SUM(salary) AS total_salary_expenditure
FROM employees
GROUP BY department_id;

--Find the maximum salary in each department.
SELECT department_id, MAX(salary) AS max_salary
FROM employees
GROUP BY department_id;

--Count the number of employees hired in each year.
SELECT YEAR(hire_date) AS hire_year, COUNT(*) AS employee_count
FROM employees
GROUP BY YEAR(hire_date);

--Determine the number of employees with the same manager.
SELECT manager_id, COUNT(*) AS employee_count
FROM employees
GROUP BY manager_id
HAVING manager_id IS NOT NULL;

--Find the average commission percentage for each department.
SELECT department_id, AVG(commission_pct) AS average_commission_pct
FROM employees
GROUP BY department_id;

--Calculate the total duration (in days) that each employee spent in their job(s) from the `job_history` table.
SELECT employee_id, SUM(DATEDIFF(end_date, start_date)) AS total_duration_in_days
FROM job_history
GROUP BY employee_id;

--Find the highest salary offered for each job title.
SELECT job_id, MAX(salary) AS highest_salary
FROM employees
GROUP BY job_id;


--JOIN

--List all employees along with their department names.
SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

--Find all employees and their job titles.
SELECT e.employee_id, e.first_name, e.last_name, j.job_title
FROM employees e
JOIN jobs j ON e.job_id = j.job_id;


--RetrieSELECT jh.employee_id, jh.start_date, jh.end_date, d.department_name
FROM job_history jh
JOIN departments d ON jh.department_id = d.department_id;
ve the job history of each employee along with the department name they worked in

--List the employees who are currently working under the same manager, displaying the manager's name.
SELECT e.employee_id, e.first_name, e.last_name, m.first_name AS manager_first_name, m.last_name AS manager_last_name
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
ORDER BY e.manager_id;

--Retrieve the details of all departments located in a specific city i.e "Tokyo".
SELECT d.department_id, d.department_name, d.location_id
FROM departments d
JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'Tokyo';

--Retrieve the details of all departments located in a specific cities i.e "Sydney" and "Toronto".

SELECT d.department_id, d.department_name, d.location_id
FROM departments d
JOIN locations l ON d.location_id = l.location_id
WHERE l.city IN ('Sydney', 'Toronto');




--### LEFT JOIN

--List all employees and their managers, including those without managers.
SELECT e.employee_id, e.first_name, e.last_name, m.first_name AS manager_first_name, m.last_name AS manager_last_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

--Find all departments and their employees, including departments with no employees.
SELECT d.department_id, d.department_name, e.employee_id, e.first_name, e.last_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;

--Retrieve a list of all job titles and the employees who have that job, including job titles with no employees.
SELECT j.job_id, j.job_title, e.employee_id, e.first_name, e.last_name
FROM jobs j
LEFT JOIN employees e ON j.job_id = e.job_id;

--### RIGHT JOIN Assignments
--Find all employees and the locations they are working in, including locations without any employees.
SELECT e.employee_id, e.first_name, e.last_name, l.location_id, l.city, l.state_province
FROM employees e
RIGHT JOIN locations l ON e.location_id = l.location_id;

--List all countries and the regions they belong to, including regions without any countries.

SELECT c.country_id, c.country_name, r.region_id, r.region_name
FROM countries c
RIGHT JOIN regions r ON c.region_id = r.region_id;



--JOIN + Group BY

--List the number of employees working in each city.
SELECT l.city, COUNT(e.employee_id) AS employee_count
FROM employees e
JOIN locations l ON e.location_id = l.location_id
GROUP BY l.city;

--List the total salary expenditure for each department, along with the department name.
SELECT d.department_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;

--Count the number of employees in each city.
SELECT l.city, COUNT(e.employee_id) AS employee_count
FROM employees e
JOIN locations l ON e.location_id = l.location_id
GROUP BY l.city;

--Calculate the average salary for each job title within each department.
SELECT d.department_name, j.job_title, AVG(e.salary) AS average_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN jobs j ON e.job_id = j.job_id
GROUP BY d.department_name, j.job_title;

--List the number of employees hired in each year for each job title.
SELECT j.job_title, EXTRACT(YEAR FROM e.hire_date) AS hire_year, COUNT(e.employee_id) AS employee_count
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title, hire_year;

--Find the highest salary paid in each region.
SELECT r.region_name, MAX(e.salary) AS highest_salary
FROM employees e
JOIN locations l ON e.location_id = l.location_id
JOIN countries c ON l.country_id = c.country_id
JOIN regions r ON c.region_id = r.region_id
GROUP BY r.region_name;

--Count the number of employees in each country.
SELECT c.country_name, COUNT(e.employee_id) AS employee_count
FROM employees e
JOIN locations l ON e.location_id = l.location_id
JOIN countries c ON l.country_id = c.country_id
GROUP BY c.country_name;

--Calculate the average salary and the number of employees for each department located in a specific region.
SELECT d.department_name, AVG(e.salary) AS average_salary, COUNT(e.employee_id) AS employee_count
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON e.location_id = l.location_id
JOIN countries c ON l.country_id = c.country_id
JOIN regions r ON c.region_id = r.region_id
WHERE r.region_name = 'Specific Region'  -- Replace with the specific region name
GROUP BY d.department_name;






































