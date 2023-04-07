SELECT A.ANIMAL_ID AS ANIMAL_ID, A.ANIMAL_TYPE AS ANIMAL_TYPE, A.NAME AS NAME
FROM ANIMAL_INS A 
    JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID 
WHERE A.SEX_UPON_INTAKE <> B.SEX_UPON_OUTCOME;


