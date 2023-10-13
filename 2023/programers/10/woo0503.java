// 너무쉬웟더 10분컷

class Problem3 {
    public int solution(String[] number) {
        int outVal = 0;
        String[] TSN = {"3", "6", "9"};
        for(String n : number){
            for (String t : TSN) {
                int temp = 0;
                if (n.equals(t)) {
                    temp += 1;
                }
                outVal += temp;
            }
        }
        return outVal;
    }
}

public class Main {
    static Problem3 solution = new Problem3();
    public static void main(String[] args) {
        int answer = 0;
        int req = 33;
        for (int i = 1; i <= req; i++) {
            String[] num = String.valueOf(i).split("");
            answer += solution.solution(num);
        }
        System.out.println(answer);

    }
}
