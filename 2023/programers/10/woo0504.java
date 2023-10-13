// 아스키코드 참고 : https://blog.naver.com/PostView.nhn?blogId=jysaa5&logNo=221831226674
// cannot convert String to char 오류 => "A".charAt(0) 과 같은 형식으로 쓰면 된당 ~ 
// https://stackoverflow.com/questions/7853502/how-to-convert-parse-from-string-to-char-in-java

class Problem4 {
    public String solution(String[] inVal) {
        String outVal = "";
        for (String n : inVal){
            if (n.equals(" ")) outVal += " ";
            else if (n.charAt(0) >= 97){
                outVal += (char) (122+97-n.charAt(0));
            }else {
                outVal += (char) (90+65-n.charAt(0));
            }
        }
        
        return outVal;
    }
}

public class Main {
    static Problem4 solution = new Problem4();
    public static void main(String[] args) {
        char sc = "a".charAt(0);
        int scToint = (int) sc;
        char iTochar = (char) (scToint+ 25);
        String[] inVal = String.valueOf("I love you").split("");
        String answer = solution.solution(inVal);
        System.out.println(answer);
    }
}
