//https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=java
public class SignMatch {
    public int signMatch (boolean[] signs, int n) {
        return signs[n]? 1:-1;
    }
}

class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        SignMatch signMatch = new SignMatch();
        int answer = 0;
        for (int i = 0; i < absolutes.length; i++) {
            answer += absolutes[i]*signMatch.signMatch(signs, i);
        }
        return answer;
    }
}
