-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A 
    JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID 
WHERE B.DATETIME < A.DATETIME 
ORDER BY A.DATETIME ASC