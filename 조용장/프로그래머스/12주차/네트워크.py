def solution(n, computers):
    answer = 0
    graph=[[] for _ in range(n+1)]
    visited=[False for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i!=j and computers[i][j]==1:
                graph[i+1].append(j+1)
    # 그래프 정리 끝!
    print(graph)
    count=0

    for i in range(1,len(computers)+1):
        if visited[i]==False:
            queue=graph[i]
            visited[i]=True
            count+=1
            while queue:
                v= queue.pop()
                if visited[v]==False:
                    visited[v]=True
                    for j in graph[v]:
                        queue.append(j)
    answer=count
    return answer