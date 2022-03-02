def solution(answers):
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    a=0
    b=0
    c=0

    
    for i, v in enumerate(answers):
        if (num1[i%len(num1)]-v)==0:
            a+=1
        if (num2[i%len(num2)]-v)==0:
            b+=1
        if (num3[i%len(num3)]-v)==0:
            c+=1

    answer = []
    if max(a,b,c)==a:
        answer.append(1)
    if max(a,b,c)==b:
        answer.append(2)
    if max(a,b,c)==c:
        answer.append(3)
    return answer