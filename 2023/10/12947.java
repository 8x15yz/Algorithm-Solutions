// https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=java
public class IsHsd {
    public boolean isHsd(int n) {
        String[] part = String.valueOf(n).split("");
        int pSum = 0;
        for (String i : part) {
            pSum += Integer.parseInt(i);
        }
        return n % pSum == 0 ? true : false;
    }
}


class Solution {
    IsHsd isHsd = new IsHsd();
    public boolean solution(int x) {
        boolean answer = isHsd.isHsd(x);
        return answer;
    }
}
