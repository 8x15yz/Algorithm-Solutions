# https://school.programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    #musicinfos = 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
    #조건이 일치하는 음악이 여러 개일 때: '재생된 시간'이 제일 긴 음악
    #네오는 항상 음악 하나만 듣는다 => 한 음악이 반복되거나 // 한 음악의 일부거나 둘중 하나
    answer = ''
    dots = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    neoListenedM = len(m)-m.count('#')
    redisginMusicinfos = []
    checkThisMusicIsAccurate = []
    for find in musicinfos:
        #0 1 3 4 6 7 9 10
        redisginMusicinfos.append([])
        startH, startM, endH, endM = int(find[0:2]), int(find[3:5]), int(find[6:8]), int(find[9:11])
        totalM = 0
        #print(startH, startM, endH, endM)
        totalM = 60-startM+endM if endH > startH else endM
        musicTitle, musicSheet = '', ''
        for i in range(12, len(find)):
            if find[i] != ',': musicTitle += find[i]
            else: 
                musicSheet = find[i+1:]
                #print(neoListenedM, totalM, musicTitle, musicSheet)
                redisginMusicinfos[-1] = [totalM, musicTitle, musicSheet]
                break
        leastLgt = min(len(musicSheet), len(m))
        if musicSheet[:leastLgt] == m[:leastLgt]: checkThisMusicIsAccurate.append([totalM, musicTitle])
        else: checkThisMusicIsAccurate.append([-1, musicTitle])
            
    maxAns = [-99, '']
    for ans in checkThisMusicIsAccurate:
        if maxAns[0] < ans[0]:
            maxAns = ans
    print(checkThisMusicIsAccurate)
    return maxAns[1]
