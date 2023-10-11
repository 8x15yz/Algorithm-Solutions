// 풀고잇는중 ..
class Problem2 {
    public static int solution(String[] input) {
        String[] answer = new String[input.length];
        System.out.println("이거요");        
        for (String i: input) {System.out.println(i);}
        // for (int i = 0; i < input.length; i++) {
        //     // answer[i] = 
        // }
        return 0;
    }
}

public class Main {
    static Problem2 solution = new Problem2();
    public static void main(String[] args) {
        String cryptogram = "browoanoommnaon";
        String[] input = String.valueOf(cryptogram).split("");
        System.out.println(solution.solution(input));        
        System.out.println("dkfj");
    }
}
