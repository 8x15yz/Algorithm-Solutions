사용법은 이렇습니다:

/algo-review
날짜: 26-04-25
문제: 두 수의 합
설명: 배열에서 합이 target인 두 수의 인덱스를 반환
코드:
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
실행하면 자동으로:

5단계 리뷰 수행
reviews/202604-두수의합.md 저장
202604.html 에 해당 날짜 섹션 찾아서 problem-item + 리뷰 토글 삽입 (날짜 섹션 없으면 새로 만들어서 삽입)
완료 보고


/algo-comment
날짜: 26-04-24
문제: 암호문
코멘트: in 'rev' 쓰면 빈 문자열도 True 반환되는 거 몰랐음. 다음엔 집합으로 쓰자