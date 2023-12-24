// https://school.programmers.co.kr/learn/courses/30/lessons/12925?language=java
// string 길이 재는 메서드는 length(); => 굳이 char배열로 안바꿔도됨
// charAt(i) 메서드 => char배열로 안바꿔도 그자리 값을 알 수 있음

public class StrToInt {
    public int getStrToInt(String str) {
        boolean Sign = true;
        int result = 0;
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch == '-') {Sign = false;}
            else if(ch !='+') {result = result * 10 + (ch - '0');}
        }
        return Sign? 1 * result:-1 * result;
    }
}

class Solution {
    public int solution(String s) {
        StrToInt strToInt = new StrToInt();
        System.out.println(strToInt.getStrToInt(s));
        int answer = 0;
        return answer;
    }
}
