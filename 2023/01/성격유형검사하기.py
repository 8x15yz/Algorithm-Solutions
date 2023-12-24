# 
# 30분

def solution(survey, choices):
    answer = ''
    sur = {}
    sur['R'] = 0
    sur['T'] = 0
    sur['C'] = 0
    sur['F'] = 0
    sur['J'] = 0
    sur['M'] = 0
    sur['A'] = 0
    sur['N'] = 0
    
    surveylist = [
        ['R', 'T'],
        ['C', 'F'],
        ['J', 'M'],
        ['A', 'N'],
    ]
    
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        elif choices[i] > 4:
            sur[survey[i][1]] += abs(4-choices[i])
        elif choices[i] < 4:
            sur[survey[i][0]] += abs(4-choices[i])
    
    for liste in surveylist:
        if sur[liste[0]] > sur[liste[1]]:
            answer += liste[0]
        elif sur[liste[0]] < sur[liste[1]]:
            answer += liste[1]
        elif sur[liste[0]] == sur[liste[1]]:
            answer += liste[0]
            
    return answer
