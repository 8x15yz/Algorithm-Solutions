// HashMap 사용하기 딕셔너리같은 개념: https://velog.io/@db_jam/Java-%ED%95%B4%EC%8B%9C%EB%A7%B5HashMap-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%A0%95%EB%A6%AC
// 해시맵에서 밸류를 두개이상의 값으로 저장하고 싶을 때 쓰는 방법 : value를 Object로 지정한다 : https://data-study-clip.tistory.com/61

import java.util.ArrayList;
import java.util.HashMap;

class Problem7 {
    public ArrayList<String> solution(String[][] friends, String[] visitors, String user) {
        ArrayList<String> result = new ArrayList<String>();
        HashMap<String, ArrayList<String>> userMaps = new HashMap<String, ArrayList<String>>();

        System.out.println(userMaps);
        return result;
    }
}

public class Main {
    static Problem7 solution = new Problem7();
    public static void main(String[] args) {
        String[][] friends = { {"donut", "andole"}, {"donut", "jun"}, {"donut", "mrko"}, {"shakevan", "andole"}, {"shakevan", "jun"}, {"shakevan", "mrko"} };
        String[] visitors = {"bedi", "bedi", "donut", "bedi", "shakevan"};
        String user = "mrko";
        
        ArrayList<String> answer = solution.solution(friends, visitors, user);
        System.out.println(answer);
    }
}
