def solution(n):
    print(n%3,n//3)
    a=[]
    while True:
        a.append(str(n%3))
        n=n//3
        if n==0:
            break
    answer = int("".join(a),3)
    return answer