# 기본적으로 이동을 못한 경우를 확인하기 위해 -1로 두었음.
answer = -1

# 같은 알파벳 개수를 세주는 함수
def word_count(a,b):
    count=0
    for i in range(len(a)):
        if a[i]==b[i]:
            count+=1
    return count

# 깊이 우선 탐색
def dfs(begin, target, words, visited, count):
    global answer # global을 사용하여 answer 값을 가져옴.
    # begin과 target이 같은경우
    if begin==target:
        if answer==-1: # 처음으로 나온것이면 answer는 count를 그대로 받아준다.
            answer = count
        elif count < answer: # 처음이 아닌경우 count와 이전의 answer를 비교하여 최소값을 answer로 저장한다.
            answer = count
    # begin과 target이 다른 경우
    else:
        # words에서 모든 알파벳을 불러온다.
        for i in range(len(words)):
            # visited를 통해 이미 들린곳은 안가고 word_count 함수를 통해 값이 begin의 개수-1과 같은 경우
            if visited[i]==False and word_count(begin,words[i])==(len(begin)-1):
                # 방문한 것으로 처리함.
                visited[i]=True
                # dfs를 다시 불러오며 begin은 words[i]로 바뀌고 count는 1 증가한다.
                dfs(words[i],target,words,visited,count+1)
                # dfs가 다 끝나고 다시 돌아왔으니 visited는 False로 변경한다.
                visited[i]=False
                    
                
def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    else:
        # 방문 여부를 알기위해 넣음.
        visited = [False for _ in range(len(words))]
        dfs(begin,target,words,visited,0)
        # 찾지 못한 경우 0으로 처리한다.
        if answer== -1:
            answer=0
        return answer