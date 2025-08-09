WITH cte AS (
    SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rank_sal
    FROM Employee
)

SELECT 
    CASE 
        WHEN COUNT(*) = 0 THEN NULL
        ELSE MAX(salary)
    END AS SecondHighestSalary
FROM cte
WHERE rank_sal = 2;
