-- # MySQL Sub Query

-- Assignment 1: Employees in Specific Departments
-- Task: Retrieve the EMPLOYEE_ID, FIRST_NAME, and LAST_NAME of employees who work in departments located in cities that start with the letter 'S'.
-- Hint: Use a subquery after the WHERE clause to find DEPARTMENT_IDs based on LOCATION_IDs from the locations table.
SELECT e.EMPLOYEE_ID, e.FIRST_NAME, e.LAST_NAME
FROM employees e
WHERE e.DEPARTMENT_ID IN (
    SELECT d.DEPARTMENT_ID
    FROM departments d
    JOIN locations l ON d.LOCATION_ID = l.LOCATION_ID
    WHERE l.CITY LIKE 'S%'
);

-- Assignment 2: High Salary Jobs
-- Task: List the JOB_ID and JOB_TITLE for jobs that have a minimum salary greater than the average salary across all jobs.
-- Hint: Use a subquery after the WHERE clause to calculate the average salary.

SELECT j.JOB_ID, j.JOB_TITLE
FROM jobs j
WHERE j.MIN_SALARY > (
    SELECT AVG(MIN_SALARY)
    FROM jobs
);

-- Assignment 3: Employee and Their Manager's Details
-- Task: Display EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and MANAGER_ID of employees along with the FIRST_NAME and LAST_NAME of their managers.
-- Hint: Use a subquery after the FROM clause to join the employees table to itself to get the manager's details.
SELECT e.EMPLOYEE_ID, e.FIRST_NAME AS EMPLOYEE_FIRST_NAME, e.LAST_NAME AS EMPLOYEE_LAST_NAME,
       m.FIRST_NAME AS MANAGER_FIRST_NAME, m.LAST_NAME AS MANAGER_LAST_NAME
FROM employees e
LEFT JOIN employees m ON e.MANAGER_ID = m.EMPLOYEE_ID;

-- Assignment 4: Departments with Employees Hired After a Specific Date
-- Task: Retrieve DEPARTMENT_ID and DEPARTMENT_NAME for departments that have employees hired after '01-JAN-2010'.
-- Hint: Use a subquery after the WHERE clause to find departments based on hire dates in the employees table.
SELECT d.DEPARTMENT_ID, d.DEPARTMENT_NAME
FROM departments d
WHERE d.DEPARTMENT_ID IN (
    SELECT e.DEPARTMENT_ID
    FROM employees e
    WHERE e.HIRE_DATE > '2010-01-01'
);

-- Assignment 5: Locations with Multiple Departments
-- Task: List LOCATION_ID and CITY for locations that have more than one department.
-- Hint: Use a subquery after the FROM clause to group and count departments per location.
SELECT l.LOCATION_ID, l.CITY
FROM locations l
WHERE l.LOCATION_ID IN (
    SELECT d.LOCATION_ID
    FROM departments d
    GROUP BY d.LOCATION_ID
    HAVING COUNT(d.DEPARTMENT_ID) > 1
);

-- Assignment 6: Employees with Maximum Salary in Their Department
-- Task: Retrieve the EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and SALARY of employees who earn the maximum salary in their respective departments.
-- Hint: Use a subquery after the WHERE clause to find the maximum salary per department.
SELECT e.EMPLOYEE_ID, e.FIRST_NAME, e.LAST_NAME, e.SALARY
FROM employees e
WHERE e.SALARY = (
    SELECT MAX(s.SALARY)
    FROM employees s
    WHERE s.DEPARTMENT_ID = e.DEPARTMENT_ID
);

-- Assignment 7: Jobs with Employees in More Than One Department
-- Task: List JOB_ID and JOB_TITLE for jobs where employees have worked in more than one department (including past jobs from the job_history table).
-- Hint: Use a subquery after the WHERE clause to check the number of distinct departments per employee from the job_history table.
SELECT j.JOB_ID, j.JOB_TITLE
FROM jobs j
WHERE j.JOB_ID IN (
    SELECT jh.JOB_ID
    FROM job_history jh
    GROUP BY jh.JOB_ID
    HAVING COUNT(DISTINCT jh.DEPARTMENT_ID) > 1
);

-- Assignment 8: Departments Without Managers
-- Task: Retrieve DEPARTMENT_ID and DEPARTMENT_NAME for departments that do not have a manager assigned.
-- Hint: Use a subquery after the WHERE clause to identify departments where MANAGER_ID is NULL.
SELECT d.DEPARTMENT_ID, d.DEPARTMENT_NAME
FROM departments d
WHERE d.MANAGER_ID IS NULL;

-- Assignment 9: Employees Hired in Regions with a Specific Name
-- Task: Display EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and HIRE_DATE of employees who were hired in regions with the name 'Europe'.
-- Hint: Use a subquery after the FROM clause to join employees with locations, countries, and regions tables.
SELECT e.EMPLOYEE_ID, e.FIRST_NAME, e.LAST_NAME, e.HIRE_DATE
FROM employees e
JOIN departments d ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
JOIN locations l ON d.LOCATION_ID = l.LOCATION_ID
JOIN countries c ON l.COUNTRY_ID = c.COUNTRY_ID
JOIN regions r ON c.REGION_ID = r.REGION_ID
WHERE r.REGION_NAME = 'Europe';

-- Assignment 10: Recent Job Changes
-- Task: List EMPLOYEE_ID, FIRST_NAME, LAST_NAME, and the latest job JOB_ID for employees who have had more than one job.
-- Hint: Use a subquery after the FROM clause to get the latest START_DATE from the job_history table.
SELECT e.EMPLOYEE_ID, e.FIRST_NAME, e.LAST_NAME, jh.JOB_ID
FROM employees e
JOIN job_history jh ON e.EMPLOYEE_ID = jh.EMPLOYEE_ID
WHERE jh.START_DATE = (
    SELECT MAX(jh2.START_DATE)
    FROM job_history jh2
    WHERE jh2.EMPLOYEE_ID = e.EMPLOYEE_ID
)
GROUP BY e.EMPLOYEE_ID
HAVING COUNT(DISTINCT jh.JOB_ID) > 1;
