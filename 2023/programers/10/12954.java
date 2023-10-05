// https://school.programmers.co.kr/learn/courses/30/lessons/12954?language=java
// array 자바 문법 참고 https://m.blog.naver.com/heartflow89/220950491600

public class FindNum {
    public long[] findNum(long x, int n) {
        long[] answer = new long[n];
        for (int i = 0; i < n; i++) {
            answer[i] = x*(i+1);
        }
        return answer;
    }
}

class Solution {
    public long[] solution(long x, int n) {
        FindNum findNum = new FindNum();
        long[] answer = findNum.findNum(x, n);
        return answer;
    }
}

// 왜 x가 long 타입 이어야 하는건가요?,,
// x * (i + 1) 을 범위 맥스치인 1000만에 놓고 n이 1000이라고 한다면 100억이기 때문에 int 안에 못 담겨서 -로 부동소수점이 돌아버려서 마이너스가 된 후 long 타입인 answer에 담기기 때문인 것 같아요
// https://school.programmers.co.kr/questions/26059 참고 
