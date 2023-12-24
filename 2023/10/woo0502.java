// inVal[i] == inVal[i-1] 이걸로는 비교할 수 없다는거 : inVal[i].equals(inVal[i-1]) 이걸로 해야 먹힘 !!!!!!!기억해 
// String[]을 String으로 : String.join() => https://developer-talk.tistory.com/451
class Problem2 {
    public static String solution(String[] inVal) {
        for(String n : inVal) {System.out.print(n);}
        System.out.println();
        int pointer = 0;
        int compare = 1;
        int[] isSame = new int[inVal.length];
        String outVal = "";
        
        while (compare < inVal.length){
            while (inVal[pointer].equals(inVal[compare])) {
                isSame[pointer] = 1;
                isSame[compare] = 1;
                compare += 1;
            }
            if (isSame[pointer] != 1) {outVal += inVal[pointer];}
            pointer = compare;
            compare += 1;
        }
        
        return outVal;
    }
}

public class Main {
    static Problem2 solution = new Problem2();
    public static void main(String[] args) {
        String cryptogram = "browoanoommnaon";
        String[] inVal = String.valueOf(cryptogram+"*").split("");
        String outVal = "";
        while (true) {    
            outVal = solution.solution(inVal)+"*";
            if (outVal.equals(String.join("", inVal)) || outVal == "") break;
            inVal = String.valueOf(outVal).split("");
        }
        System.out.print("the Answer IS : ");        
        System.out.println(outVal);

    }
}
