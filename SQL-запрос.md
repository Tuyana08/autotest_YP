# Работа с базой данных

## Задание 1

SQL-Запрос:
```sql
SELECT c.login, Count(o."inDelivery") AS "OrderCount" 
FROM "Couriers" AS c LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true 
GROUP BY c.login;
```

## Задание 2

SQL-Запрос:
```sql
SELECT track, 
    CASE 
        WHEN finished = true THEN 2 
        WHEN cancelled = true THEN -1 
        WHEN "inDelivery" = true THEN 1 
        ELSE 0 
        END AS status 
FROM "Orders";
```