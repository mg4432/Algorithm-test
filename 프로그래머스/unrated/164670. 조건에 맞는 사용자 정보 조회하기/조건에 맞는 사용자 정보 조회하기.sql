# -- 코드를 입력하세요
# SELECT count(*) as cnt, A.WRITER_ID as ID
# FROM USED_GOODS_BOARD A 
#     JOIN USED_GOODS_USER B ON A.WRITER_ID = B.USER_ID
# GROUP BY A.WRITER_ID
# ;

SELECT A.WRITER_ID AS USER_ID, B.NICKNAME AS NICKNAME, 
      CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소,
      CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO, 4, 4), '-', SUBSTR(TLNO, 8, 4)) AS 전화번호
FROM USED_GOODS_BOARD A 
    JOIN USED_GOODS_USER B ON A.WRITER_ID = B.USER_ID
GROUP BY A.WRITER_ID
HAVING COUNT(*) >= 3
ORDER BY USER_ID DESC
;