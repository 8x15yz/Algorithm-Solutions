// 캐스팅 연습 참고 https://mainia.tistory.com/2020

public class GetMean {
    public double getMean(int[] array) {
      int Sum = 0;
      for(int i = 0; i < array.length; i++){
                 Sum = Sum + array[i];
      }
        return Sum / (double) array.length;
    }
}


class Solution {
    public double solution(int[] arr) {
        GetMean getMean = new GetMean();
        return getMean.getMean(arr);
    }
}
