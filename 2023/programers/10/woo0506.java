// ArrayList 사용 : https://hianna.tistory.com/568
// 완전탐색
import java.util.ArrayList;
import java.util.Arrays;


class Problem6 {
    public ArrayList<String> solution(String[][] inVal) {
        ArrayList<String> outVal = new ArrayList<String>();
        for(int i = 0; i < inVal.length; i++){
            for(int k = 0; k < inVal[i][1].length()-1; k++){
                String pntStr = inVal[i][1].valueOf(k)+inVal[i][1].valueOf(k+1);
                for(int j = i+1; j < inVal.length; j++){ // 겹치면 이 부분에서 break
                    for(int l = 0; i < inVal[j][1].length()-1; j++){
                        String comStr = inVal[j][1].valueOf(l)+inVal[j][1].valueOf(l+1);
                        if (pntStr.equals(comStr)) {
                            outVal.add(inVal[i][0]);
                            outVal.add(inVal[j][0]);
                            break;
                        }
                    }
                }
            }
        }
        return outVal;
    }
}

public class Main {
    static Problem6 solution = new Problem6();
    public static void main(String[] args) {
        String[][] inVal = { {"jm@email.com", "제이엠"}, {"jason@email.com", "제이슨"}, {"woniee@email.com", "워니"}, {"mj@email.com", "엠제이"}, {"nowm@email.com", "이제엠"} };
        ArrayList<String> answer = solution.solution(inVal);
        System.out.println(answer);
    }
}
