# https://school.programmers.co.kr/learn/courses/30/lessons/17683

## 처음 풀이 0406 ##############################################################################################
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


## 이어서 풀다가 만거 ##############################################################################################
def solution(m, musicinfos):
    #musicinfos = 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
    #조건이 일치하는 음악이 여러 개일 때: '재생된 시간'이 제일 긴 음악
    #네오는 항상 음악 하나만 듣는다 => 한 음악이 반복되거나 // 한 음악의 일부거나
    answer = ''
    dots = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    neoListenedM = len(m)-m.count('#')
    redisginMusicinfos = []
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
                
        checkThisMusicIsAccurate = []
        #neoListenedM 네오가 들은 시간
        checkIfDotHaveShop = ['C', 'D', 'F', 'G', 'A']
        # C D F G A => #을 한번 더 검사해야됨
        ## 일치하면 [시간, 제목] append 아니면 [-1, 제목]
        msFdot = musicSheet[:2] if musicSheet[1] == '#' else musicSheet[0]
        compareing = len(msFdot)
        for dot in range(neoListenedM):
            if m[dot:dot+compareing] == msFdot:
                pass
    ## 정답 가져오는 부분
    maxAns = [-99, '']
    for ans in checkThisMusicIsAccurate:
        if maxAns[0] < ans[0]:
            maxAns = ans
    print(checkThisMusicIsAccurate)
    return maxAns[1]



## 0410 푸는중 83점 ##############################################################################################
dots = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "E#", "B#"]
dotsdict = {"C":0, "C#":1, "D":2, "D#":3, "E":4, "F":5, "F#":6, "G":7, "G#":8, "A":9, "A#":10, "B":11, "E#":12, "B#":13}

def encoding(view):
    musicSheet = []
    for j in range(len(view)):
        if j < len(view)-1 and view[j+1] == "#": musicSheet.append(dotsdict[view[j:j+2]])
        elif view[j] == "#": continue
        else: musicSheet.append(dotsdict[view[j]])
    return musicSheet

def solution(m, musicinfos):
    maxPlayTime = -99
    answer = ''
    m = encoding(m)
    for find in musicinfos:
        startH, startM, endH, endM = int(find[0:2]), int(find[3:5]), int(find[6:8]), int(find[9:11])
        totalM = (60-startM+endM)+(endH-startH-1)*60 if endH > startH else endM
        musicTitle, musicSheet = '', ''
        for k in range(12, len(find)):
            if find[k] != ',': musicTitle += find[k]
            else: 
                musicSheet = encoding(find[k+1:])
                if totalM < len(musicSheet): musicSheet = musicSheet[:totalM]
                musicSheetM = len(musicSheet)
                for i in range(musicSheetM):
                    if m[0] == musicSheet[i]:
                        sheetId = i
                        for neo in m:
                            if neo != musicSheet[sheetId]: break
                            else: sheetId = 0 if sheetId == musicSheetM-1 else sheetId + 1
                        else: 
                            if maxPlayTime < totalM: maxPlayTime, answer = totalM, musicTitle
                            break
                else: break
                
    if answer == '': answer = '(None)'
    return answer
