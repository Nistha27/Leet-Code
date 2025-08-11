WITH cte as (
    SELECT user_id,
    ROUND(SUM(action='confirmed')/COUNT(*),2) AS confirmation_rate
    FROM Confirmations
    GROUP BY user_id

)

SELECT u.user_id,coalesce(c.confirmation_rate,0.00) as confirmation_rate
FROM Signups u
LEFT JOIN cte c
ON u.user_id=c.user_id
