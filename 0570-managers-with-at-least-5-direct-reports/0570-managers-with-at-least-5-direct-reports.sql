# Write your MySQL query statement below




SELECT e.name
FROM employee e
JOIN employee m
ON e.id=m.managerId
GROUP BY m.managerId
HAVING Count(e.id)>=5