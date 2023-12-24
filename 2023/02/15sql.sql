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


# 동물의 아이디와 이름
# https://school.programmers.co.kr/learn/courses/30/lessons/59403
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


# 여러 기준으로 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/59404
# 이름은 오름차순으로, 같은 이름이 있으면 날짜는 내림차순으로
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC


# 모든 레코드 조회하기
# https://school.programmers.co.kr/learn/courses/30/lessons/59034
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


# 역순 정렬하기 => DESC 내림차순
# https://school.programmers.co.kr/learn/courses/30/lessons/59035
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC


# 이름이 없는 동물의 아이디
# https://school.programmers.co.kr/learn/courses/30/lessons/59039
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID ASC

# 최댓값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/59415
SELECT MAX(DATETIME)
FROM ANIMAL_INS

