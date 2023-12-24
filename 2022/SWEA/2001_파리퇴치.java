// 리팩터링 코드 => 메서드 만들고 불러오는 코드로도 만들어보기
import java.util.Scanner;
import java.util.Arrays;

public class Solution {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int T = input.nextInt();
		
		for (int tc = 0; tc < T; tc++) {
			int N = input.nextInt();
			int M = input.nextInt();
			int[][] arr = new int[N][N];
			
			for (int i=0; i<N; i++) {
				for (int j=0; j<N; j++) {
					arr[i][j] = input.nextInt();
				}
			}
			
			int max = 0;
			
			for (int i=0; i<N-M+1; i++) {
				for (int j=0; j<N-M+1; j++) {
					int pariSum = 0;
					for (int verti = 0; verti < M; verti++) {
						for (int hori = 0; hori < M; hori++) {
							pariSum += arr[i + verti][j + hori];
						}
					}
					if (pariSum > max) {
						max = pariSum;
					}
				}
			}
		System.out.printf("#%d %d", tc+1, max);
		System.out.println("");
			
		}
	}
}
