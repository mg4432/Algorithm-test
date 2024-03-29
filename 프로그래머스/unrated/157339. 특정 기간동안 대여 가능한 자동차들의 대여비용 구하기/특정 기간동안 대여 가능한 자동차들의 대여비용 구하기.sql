-- 코드를 입력하세요

WITH 
temp AS 
(SELECT DISTINCT(A.CAR_ID), A.CAR_TYPE, ROUND((100 - C.DISCOUNT_RATE)*0.3*A.DAILY_FEE) AS FEE
FROM CAR_RENTAL_COMPANY_CAR A 
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B ON A.CAR_ID = B.CAR_ID 
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C ON A.CAR_TYPE = C.CAR_TYPE
WHERE A.CAR_ID NOT IN ((SELECT DISTINCT(A.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR A 
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B ON A.CAR_ID = B.CAR_ID 
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C ON A.CAR_TYPE = C.CAR_TYPE
WHERE '2022-11' BETWEEN DATE_FORMAT(B.START_DATE, '%Y-%m') AND DATE_FORMAT(B.END_DATE, '%Y-%m')
)) AND  A.CAR_TYPE IN ('세단', 'SUV')  AND C.DURATION_TYPE = '30일 이상' 
AND '2022-11' NOT BETWEEN DATE_FORMAT(B.START_DATE, '%Y-%m') AND DATE_FORMAT(B.END_DATE, '%Y-%m')
)
SELECT  *
FROM temp
WHERE 500000 <= FEE AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC
