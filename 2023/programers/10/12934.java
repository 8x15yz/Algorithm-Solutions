// int자료형보다 값이 커질것같으면 long을 쓰는게 좋다

public class IsMul {
    public long isMul(long n) {
        long root = (long) Math.pow(n, 0.5);
        if (Math.pow(root, 2) == n) return (long) Math.pow(root+1, 2);
        return -1;
    }
}
class Solution {
    public long solution(long n) {
        IsMul isMul = new IsMul();
        long answer = isMul.isMul(n);
        return answer;
    }
}
