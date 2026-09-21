SELECT employees.name, departments.name AS department
FROM employees
JOIN departments
ON employees.department_id = departments.id;