def solution(answers):
    
    supo_1 = [1,2,3,4,5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    
    for answer in answers:
        if answer == supo_1[((cnt+len(supo_1))%(len(supo_1)))]:
            count_1 += 1
        if answer == supo_2[((cnt+len(supo_2))%(len(supo_2)))]:
            count_2 += 1
        if answer == supo_3[((cnt+len(supo_3))%(len(supo_3)))]:
            count_3 += 1
        cnt += 1
    
    lists = [count_1, count_2, count_3]
    answer = []
    
    for i in range(0,3):
        if lists[i] == max(lists):
            answer.append(i+1)
            
    
    return answer
