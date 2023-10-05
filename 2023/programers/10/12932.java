// https://school.programmers.co.kr/learn/courses/30/lessons/12932?language=java
// 1. 정수형 => 문자열 => 문자배열 변환하고 
// 2. answer배열 생성 후 문자배열은 끝부터 answer 배열은 처음부터 조회하면서 답을 추가하기
public class ReverseArr {
    public long[] reverseArr(String input) {
        char[] nArr = input.toCharArray();
        int Lth = nArr.length;
        long[] returnArr = new long[Lth];
        
        for (int i = Lth; i > 0 ; i--) {
            returnArr[i-1] = (int) nArr[Lth-i] - '0';
        }
        return returnArr;
    }
}

class Solution {
    public long[] solution(long n) {
        ReverseArr reverseArr = new ReverseArr();
        String input = n + "";
        long[] answer = reverseArr.reverseArr(input);
        return answer;
    }
}
