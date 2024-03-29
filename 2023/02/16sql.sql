# 강원도에 위치한 생산공장 출력
# https://school.programmers.co.kr/learn/courses/30/lessons/131112
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE "강%"
ORDER BY FACTORY_ID ASC


# 경기도에 위치한 식품창고 목록 출력
# https://school.programmers.co.kr/learn/courses/30/lessons/131114
# 풀이1
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
    CASE 
	WHEN FREEZER_YN IS NULL 
	THEN "N"
	ELSE FREEZER_YN
    END AS FREEZER_YN
FROM FOOD_WAREHOUSE 
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID;


# 풀이2
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N')
FROM FOOD_WAREHOUSE
WHERE WAREHOUSE_NAME LIKE '%경기%'
ORDER BY WAREHOUSE_ID


# 풀이3
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE FREEZER_YN IS NOT NULL AND WAREHOUSE_NAME LIKE '%경기%'
UNION ALL
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 'N'
FROM FOOD_WAREHOUSE
WHERE FREEZER_YN IS NULL AND WAREHOUSE_NAME LIKE '%경기%'
ORDER BY WAREHOUSE_ID


# 풀이4
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, COALESCE(FREEZER_YN, 'N')
FROM FOOD_WAREHOUSE
WHERE WAREHOUSE_NAME LIKE '%경기%'
ORDER BY WAREHOUSE_ID
