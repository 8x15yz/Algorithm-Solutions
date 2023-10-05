public class SumDivision {
    public int sumDivision(int num) {
        int answer = 0;
        for (int i = 1; i <= num; i++) {
            if (num%i == 0) {
                // System.out.println(i);
                answer += i;
            }
        }
        return answer;
    }
}

class Solution {
    public int solution(int n) {
        SumDivision sumDivision = new SumDivision();
        int answer = sumDivision.sumDivision(n);
        return answer;
    }
}
