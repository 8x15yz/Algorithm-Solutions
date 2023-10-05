// https://school.programmers.co.kr/learn/courses/30/lessons/87389?language=java
// 점점 익숙해지고 있다 ...!!!!
// https://wikidocs.net/212 자바 while문법 참고

public class FindNum {
    public int findNum(int num) {
        int i = 2;
        while (true) {
            if (num%i == 1) {
                return i;
            }
            else { i += 1; }
        }
    }
}

class Solution {
    public int solution(int n) {
        FindNum findNum = new FindNum();
        int answer = findNum.findNum(n);
        return answer;
    }
}
