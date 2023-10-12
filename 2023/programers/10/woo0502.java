// 풀고잇는중 ..
// 파이썬으로 갈기고 싶다 이 문제
// input[i] == input[i-1] 이걸로는 비교할 수 없다는거 : input[i].equals(input[i-1]) 이걸로 해야 먹힘 !!!!!!!기억해 
// String[]을 String으로 : String.join() => https://developer-talk.tistory.com/451

class Problem2 {
    public static String solution(String[] input) {
        String output = "";
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
        return output;
    }
}

public class Main {
    static Problem2 solution = new Problem2();
    public static void main(String[] args) {
        String cryptogram = "zyelleyz" + " ";
        String[] input = String.valueOf(cryptogram).split("");
        String sResult = "";
        while (true) {    
            sResult = solution.solution(input)+" ";
            System.out.println(sResult);
            if (sResult.equals(String.join("", input)) || sResult == "") break;
            input = String.valueOf(sResult).split("");
        }
        System.out.println(sResult);
    }
}
