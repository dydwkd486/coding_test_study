import heapq
def solution(operations):
    maxh = []
    minh = []
    deteted = set()
    v_max = 0
    v_min = 0
    for i in operations:
        temp1,temp2 = i.split()
        if temp1 == "I":
            heapq.heappush(maxh,-int(temp2))
            heapq.heappush(minh,int(temp2))
        else:
            
            if temp2 == "1" and maxh:
                while maxh:
                    v= -heapq.heappop(maxh)
                    if v not in deteted:
                        break
                deteted.add(v)
            elif temp2 == "-1" and minh:
                while minh:
                    v= heapq.heappop(minh)
                    if v not in deteted:
                        break
                deteted.add(v)

    while maxh:
        v = -heapq.heappop(maxh)
        if v not in deteted:
            v_max = v
            break
    while minh:
        v = heapq.heappop(minh)
        if v not in deteted:
            v_min = v
            break

    return [v_max,v_min]