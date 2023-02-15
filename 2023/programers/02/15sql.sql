# 이름이 있는 동물의 아이디
# https://school.programmers.co.kr/learn/courses/30/lessons/59407
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME != 'NULL'


# 아픈 동물 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/59036
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID


# 상위 n개  레코드
# https://school.programmers.co.kr/learn/courses/30/lessons/5940
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1


# 어린 동물 찾기 
# https://school.programmers.co.kr/learn/courses/30/lessons/59037
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION not in ("Aged")
ORDER BY ANIMAL_ID ;
