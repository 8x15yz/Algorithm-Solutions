// 풀고잇는중 ..

// input[i] == input[i-1] 이걸로는 비교할 수 없다는거 : input[i].equals(input[i-1]) 이걸로 해야 먹힘 !!!!!!!기억해 
// String[]을 String으로 : String.join() => https://developer-talk.tistory.com/451
class Problem2 {
    static String output = "";
    public static String solution(String[] input) {
        int pointer = 0;
        int compare = 1;
        boolean isEnd = false;
        boolean isSame = false;
        
        while (isEnd == false) {            
            while (input[pointer].equals(input[compare]) && !isEnd) {
                compare += 1;
                isSame = true;
                if (compare == input.length){isEnd = true;}
            }
            if (!isSame) {
                output += input[pointer];
            }
            isSame = false;
            pointer = compare;
            compare += 1;
            if (compare == input.length || pointer == input.length){isEnd = true;}
            
        }
        // System.out.println(output); 
        return output;
    }
}

public class Main {
    static Problem2 solution = new Problem2();
    public static void main(String[] args) {
        String cryptogram = "browoanoommnaon" + " ";
        String[] input = String.valueOf(cryptogram).split("");
        String sResult = "";
        for (int k = 0; k < 3; k++) {     
            System.out.println("결과");
            System.out.println(sResult);
            System.out.println(String.join("", input));
            sResult = "";
            sResult = solution.solution(input);
            input = String.valueOf(sResult).split("");
            System.out.println(String.join("", input));
            if (sResult.equals(input)) break;
            
        }
    }
}
