# https://school.programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees_set):
    answer = 0
    for skill_trees in skill_trees_set:
        prioritySkill = {}
        i = 0
        isLearned = []
        for sk in skill:
            prioritySkill[sk] = i
            isLearned += [0]
            i += 1
        isLearned[0] = "miL"
        for sk in skill_trees:
            print(sk, isLearned)
            if sk in prioritySkill:
                if isLearned[prioritySkill[sk]] == "Learned": continue
                elif isLearned[prioritySkill[sk]] == "miL":
                    isLearned[prioritySkill[sk]] = "Learned"
                    if prioritySkill[sk] == len(skill)-1:
                        answer += 1
                        break
                    else:isLearned[prioritySkill[sk]+1] = "miL"
                else: break
        else: answer += 1
        
    return answer
