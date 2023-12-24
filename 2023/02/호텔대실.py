# https://school.programmers.co.kr/learn/courses/30/lessons/155651?language=python3

# 틀린코드
def solution(book_time):
    InOuty, checked = [], [0 for _ in range(len(book_time))]
    
    for i in range(len(book_time)):
        InOuty.append((int(book_time[i][0][:2])*60 + int(book_time[i][0][3:])
                      ,(int(book_time[i][1][:2])*60 + int(book_time[i][1][3:])+10)))
    InOuty = sorted(InOuty, key=lambda x:x[0])
    
    hotel = [[(0, 0)]]
    for i in range(len(InOuty)):
        for room in range(len(hotel)):
            if hotel[room][-1][1] <= InOuty[i][0]:
                hotel[room].append(InOuty[i])
            else:
                hotel.append([InOuty[i]])
                #break <= 여기에서 에러남
    return len(hotel)



# 완전 바보같았던거임
# 정답코드
def solution(book_time):
    InOuty = []
    
    for i in range(len(book_time)):
        InOuty.append((int(book_time[i][0][:2])*60 + int(book_time[i][0][3:])
                      ,(int(book_time[i][1][:2])*60 + int(book_time[i][1][3:])+10)))
    InOuty = sorted(InOuty, key=lambda x:x[0])
    
    hotel = [[(0, 0)]]
    for i in range(len(InOuty)):
        for room in range(len(hotel)):
            if hotel[room][-1][1] <= InOuty[i][0]:
                hotel[room].append(InOuty[i])
                break
        else:
            hotel.append([InOuty[i]])
    return len(hotel)
