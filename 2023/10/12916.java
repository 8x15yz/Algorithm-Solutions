// https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=java
// bool 자료형 : boolean 으로 씀

public class FindChar{
    public boolean findChar(String s) {
        int p = 0;
        int y = 0;
        char[] ctring = s.toCharArray();
        for (int i = 0; i < ctring.length; i++) {
            if (ctring[i] == 'p' || ctring[i] == 'P') { p += 1; }
            else if (ctring[i] == 'y' || ctring[i] == 'Y') { y += 1; }
        }
        if (p == y) { return true; }
        else { return false; }
    }
}


class Solution {
    boolean solution(String s) {
        boolean answer = true;
        FindChar findChar = new FindChar();
        answer = findChar.findChar(s);
        return answer;
    }
}
