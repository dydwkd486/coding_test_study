import heapq
def solution(jobs):
    h =[]
    p=[]
    count = 0
    result =0
    # 처음에는 소요시간 기준으로 우선순위 큐 정렬을 한다.
    for i in jobs:
        heapq.heappush(h,i)
    # 우선순위 큐에서 작업의 소요시간까지 돌리고 작업이 요청되는 시점이 포함되는 곳에 옮겨준다.
    
    # 제일 먼저 나와있는 값을 수행한다
    v= heapq.heappop(h)
    count= v[0]+v[1]
    result = v[1]
    # 정렬된 h가 끝날때까지 돌게 한다.
    while h:
        # 제일 먼저 나오는 작업 요청인것을 확인한다.
        v= h[0]
        # 작업 완료 시간보다 작은 경우를 p에 우선순위 큐로 집어 넣음.
        if count>=v[0]:
            heapq.heappop(h)
            heapq.heappush(p,[v[1],v[0]])
         # 작업시간을 초과한 경우
        else:
            # p가 있는 경우
            if p:
                temp = heapq.heappop(p)
                result +=count-temp[1]+temp[0] 
                count+=temp[0]
            # p가 없다는 것은 작업할 것이 없다는 것으로 1초를 늘려준다.
            else:
                count+=1
            
    
    # 정렬된 p 남은 것을 다 돌림.
    while p:
        temp = heapq.heappop(p)
        result +=count-temp[1]+temp[0] 
        count+=temp[0]
    
    answer = result//len(jobs)
    return answer