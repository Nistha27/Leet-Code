# Write your MySQL query statement below
SELECT user_id , CONCAT(UCASE(Left(name,1)),LCASE(Substring(name,2))) AS name
FROM Users
ORDER BY user_id