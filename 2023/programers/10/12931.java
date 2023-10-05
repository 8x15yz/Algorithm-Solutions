// https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=java
// 형변환 참고 https://sophia2730.tistory.com/entry/JAVA-int-char-String-%ED%98%95%EB%B3%80%ED%99%98-%EC%A0%95%EB%A6%AC
// 문자열 순회 참고 : 문자열에서 문자 배열로 만들고 그걸 순회해야됨 https://www.freecodecamp.org/korean/news/munjayeoleseo-munja-baeyeolro-java-tyutorieol/

public class SumEachNum {
    public int sumEachNum(String num) {
        int answer = 0;
        char[] arrNum = num.toCharArray();
        
        for (int i = 0; i < arrNum.length; i++) {
            answer += (int) arrNum[i] - '0';
        }
        return answer;
    }
}

class Solution {
    public int solution(int n) {
        SumEachNum sumEachNum = new SumEachNum();
        String num = n + "";
        int answer = sumEachNum.sumEachNum(num);
        return answer;
    }
}
