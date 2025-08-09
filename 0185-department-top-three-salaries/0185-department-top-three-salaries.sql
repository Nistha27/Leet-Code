WITH cte as (SELECT d.name as Department , e.name as Employee ,e.salary,
DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) as rank_n
FROM Employee as e
LEFT JOIN Department as d
ON e.departmentID = d.id)

SELECT Department, Employee,Salary 
FROM cte
WHERE rank_n <4
ORDER BY Salary DESC

