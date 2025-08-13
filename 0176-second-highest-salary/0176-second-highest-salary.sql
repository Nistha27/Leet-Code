SELECT 
CASE 
WHEN Count(*)=0 THEN NULL
ELSE max(salary) 
END AS SecondHighestSalary
FROM Employee
WHERE salary<(SELECT MAX(salary) from Employee)

