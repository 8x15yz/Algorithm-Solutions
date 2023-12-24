// https://school.programmers.co.kr/learn/courses/30/lessons/12933?language=java
// https://codechacha.com/ko/java-sorting-array/ 자바 배열 정렬
// String.valueOf() 메서드 : 괄호안의 객체를 string으로 변환시킴
// java.util.* 에 대해 : https://okky.kr/questions/36658
// StringBuilder : 자바에서는 string객체를 생성하면 변경이 불가한데 스트링빌더는 변경가능한 문자열을 만들어주는 방법임

import java.util.*;
class Solution {
  public long solution(long n) {
        String[] list = String.valueOf(n).split("");
        Arrays.sort(list);

        StringBuilder sb = new StringBuilder();
        for (String a : list) sb.append(a);

        return Long.parseLong(sb.reverse().toString());
  }
}
