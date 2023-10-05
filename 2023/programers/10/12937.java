// 나머지연산자 참고 https://initstory.tistory.com/56
public class GetNum {
    public String getNum(int num) {
        String answer = "";
        if (num % 2 == 1) {
            answer = "Odd";
        }
        else {
            answer = "Even";
        }
        return answer;
    }
}

class Solution {
    public String solution(int num) {
        GetNum getNum = new GetNum();
        return getNum.getNum(num);
    }
}

