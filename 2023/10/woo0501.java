// 자바에서 정수어레이 다루기 https://www.techiedelight.com/ko/convert-list-integer-array-int/
// array / list 차이 https://suzyalrahala.tistory.com/24 => list는 인덱스가 없음!!!
// https://caileb.tistory.com/190 array List 차이
// Arrays.asList() 메서드: 일반 배열을 ArrayList로 변환한다 => https://m.blog.naver.com/roropoly1/221140156345
// 리스트에서는 인덱스를 이용한 for문을 사용하면 안됨

// 근데 예외사항이 뭘까 .. ??
package project;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

class Problem1 {
    public static int solution(List<Integer> pobi, List<Integer> crong) {
        // pobi win 1  crong win 2
        // match 0     except -1
        int pobiNum = makeNumber(pobi);
        int crongNum = makeNumber(crong);
        if (pobiNum > crongNum) { return 1; }
        else if (pobiNum < crongNum) { return 2; }
        else if (pobiNum == crongNum) { return 0; }
        return -1;
    }
    
    public static int makeNumber(List<Integer> who) {
        int maxNum = 0;
        for (Integer i : who) {
            int nSum = 0;
            int nMul = 1;
            String[] listStr = String.valueOf(i).split("");
            for (String j : listStr) {
                int parsedJ = Integer.parseInt(j);
                nSum += parsedJ;
                nMul *= parsedJ;
            }
            if (maxNum < nSum) {maxNum = nSum;}
            if (maxNum < nMul) {maxNum = nMul;}
        }
        return maxNum;
    };
}

public class Main {
    static Problem1 solution = new Problem1();
    public static void main(String[] args) {
        List<Integer> pobi = new ArrayList<Integer>();
        List<Integer> crong = new ArrayList<Integer>();
        
        int[] pobiLeft = {97, 131, 99};
        int[] pobiRight = {98, 132, 102};
        int[] crongLeft = {197, 211, 211};
        int[] crongRight = {198, 212, 212};
        for (int k = 0; k < 3; k++) {
            pobi = Arrays.asList(pobiLeft[k], pobiRight[k]); 
            crong = Arrays.asList(crongLeft[k], crongRight[k]);
            System.out.println(solution.solution(pobi, crong));
        }
    }
}
