import heapq
def solution(scoville, K):
    h = []
    count=0
    # 처음 우선 순위 큐에 집어 넣기
    for i in scoville:
        heapq.heappush(h,i)
    # 최소가 K 이상 이 나올 때까지 돌린다.
    while h[0]<K :
        # 우선순위큐의 리스트가 2보다 작은 경우 -1로 출력
        if len(h)<2:
            count=-1
            break
        # 최소인 힙을 두개 꺼낸다.
        v1= heapq.heappop(h)        
        v2= heapq.heappop(h)
        # 최소인 두개의 값을 조건에 맞게 섞는다
        temp = v1+(v2*2)
        # 섞은 값을 다시 우선순위 큐에 집어 넣는다.
        heapq.heappush(h,temp)
        count+=1
    
    answer = count
    
    return answer