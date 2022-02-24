def solution(n):
    answer = "".join(["수박" for i in range(n//2)])
    if n%2==1:
        answer+="수"
    return answer