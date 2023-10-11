// https://school.programmers.co.kr/learn/courses/30/lessons/12912?language=java
public class RangeSum {
    public long rangeSum(int a, int b) {
        long answer = 0;
        for (int i = a; i <= b; i++) {
            answer += i;
        }
        return answer;
    }
}
class Solution {
    public long solution(int a, int b) {
        RangeSum rangeSum = new RangeSum();
        int temp = 0;
        if (a > b) {
            temp = a;
            a = b;
            b = temp;
        }
        long answer = rangeSum.rangeSum(a, b);
        return answer;
    }
}
