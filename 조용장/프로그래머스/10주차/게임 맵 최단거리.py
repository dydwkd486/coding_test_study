from collections import deque
def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    n = len(maps)
    m = len(maps[0])
    visited = []
    for i in range(n):
        visited.append([-1]*m)
    
    queue = deque()
    queue.append([0,0])
    
    visited[0][0]=1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and maps[nx][ny]==1:
                if visited[nx][ny]==-1:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append([nx,ny])

    answer=visited[n-1][m-1]
    return answer