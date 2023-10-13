// 그리디
// 배열 출력하기 : https://seongsillvanas.tistory.com/9
import java.util.Arrays;
class Problem5 {
    public long[] solution(long inVal) {
        int[] won = {50000, 10000, 5000, 1000, 500, 100, 50, 10, 1};
        long[] outVal = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        for (int pointer = 0; pointer < 9; pointer++) {
            if (inVal/won[pointer] > 0){
                outVal[pointer] = inVal/won[pointer];
                inVal -= (inVal/won[pointer])*won[pointer];
            }
        }
        return outVal;
    }
}

public class Main {
    static Problem5 solution = new Problem5();
    public static void main(String[] args) {
        long inVal = 50237;
        long[] answer = solution.solution(inVal);
        System.out.println(Arrays.toString(answer));
    }
}
