import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    
    while(heap is not None):
        min = heapq.heappop(heap)
        if min >= K:
            break
        if len(heap)<1:
            answer = -1
            break
        Secondmin = heapq.heappop(heap)
        heapq.heappush(heap, min + Secondmin * 2)
        answer+=1
        
    return answer