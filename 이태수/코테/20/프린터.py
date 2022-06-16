def solution(priorities, location):
    req = []
    
    
    temp = 0
    temp = priorities.pop(0)
    i = 0
    count = 0
    answer = 0
    while 1:
        
        if temp < max(priorities):
            priorities.append(temp)
            #print("priorities = ", priorities)
            if i == location:
                i = 0
                location = len(priorities)
        else:
            req.append(temp)
            #print("req = ",req)
            if i == location:
                answer = count
            else:
                count += 1
            #print(count)
        i += 1
        
        temp = priorities.pop(0)
        if not len(priorities):
            if i == location:
                answer = count
            break

    
    
    
    return answer + 1