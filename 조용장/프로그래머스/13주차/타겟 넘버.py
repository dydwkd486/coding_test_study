result=[]
def dfs(numbers,count,num_sum):
    global result
    if len(numbers)==count:
        result.append(num_sum)
    else:
        dfs(numbers,count+1,num_sum+numbers[count])
        dfs(numbers,count+1,num_sum-numbers[count])
    
def solution(numbers, target):
    answer = 0
    global result
    num_sum=0
    dfs(numbers,0,0)
    answer=result.count(target)
    
    return answer