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
        for room in hotel:
            if room[-1][1] <= InOuty[i][0]:
                room.append(InOuty[i])
            else:
                hotel.append([InOuty[i]])
                break

    return len(hotel)
