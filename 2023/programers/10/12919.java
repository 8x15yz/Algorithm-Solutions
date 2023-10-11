public class SeoBang{
    public int seoBang(String[] seoul) {
        int i = 0;
        for (String kim : seoul) {
            if (kim.equals("Kim")) break;
            i += 1;
        }
        return i;
    }
}
class Solution {
    public String solution(String[] seoul) {
        SeoBang seoBang = new SeoBang();
        int answer = seoBang.seoBang(seoul);
        return "김서방은 "+ answer +"에 있다";
    }
}
