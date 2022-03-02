def solution(s):
    answer = 0
    a=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(len(a)):
        s=s.replace(a[i],str(i))
    answer=int(s)
    return answer