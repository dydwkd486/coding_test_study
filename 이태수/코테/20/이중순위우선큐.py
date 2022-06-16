import heapq
import re

def solution(operations):
    answer = []
    top = []
    Max_top = []
    
    for i in operations:
        print(i)
        if i.startswith('I'):
            heapq.heappush(top, re.sub(r'[^-1-9]', '', i))
            print(top)
        elif re.match(i, 'D1'):
            print("DD")
            for item in top:
                heapq.heappush(Max_top, -item)
            top = []
            heapq.heappop(Max_top)
            for item in Max_top:
                heapq.heappush(top, -heapq.heappop(Max_top))                
        elif i == ('D -1'):
            print("D -1")
            heapq.heappop(top)
        

    if len(top) == 0:
        answer = [0,0]
    elif len(top) == 1:
        answer = [top[0],top[0]]
    else:
        answer = [max(top),min(top)]
    return answer