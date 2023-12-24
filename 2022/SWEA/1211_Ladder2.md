[Ladder2의 주소](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

1. 제일먼저 0행에 값이 1인 index만 시작점이 될수있도록 for와 if를 섞어서 조건을 걸어줌
2. 그리고 min값(최단거리)은 무한대로 초기화, minDex(최단거리인 시작인덱스)도 0으로 초기화해줌
3. 이후는 Ladder1과 같이 방문리스트 만들고 조건걸어주면서 델타탐색 진행, 거리재야하므로 한칸 앞서나갈때마다 cnt를 1 누적함
4. 근데 이때 최단거리를 구하기 때문에 나름의 가지치기를 위해 한칸 앞서나갈때마다 min값과 cnt를 비교하면서 cnt가 min을 넘어가면 break하도록 함
5. 그렇게 min보다 적은 경로가 나오면 minDex 변경하는 로직으로 전반적인 코드를 구성함
