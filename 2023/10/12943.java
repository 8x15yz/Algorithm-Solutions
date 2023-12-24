// 자바의 첫 재귀 ~
// https://school.programmers.co.kr/learn/courses/30/lessons/12943?language=java
public class Collatz{
    static long cnt = -1;
    public long collatz(long n) {
        cnt += 1;
        if (n == 1) return cnt;
        else if (cnt == 500) return -1;
        else if (n % 2 == 0) return collatz(n/2);
        else return collatz((n*3)+1);
    }
}

class Solution {
    Collatz collatz = new Collatz();
    public long solution(long num) {
        long answer = collatz.collatz(num);
        return answer;
    }
}
