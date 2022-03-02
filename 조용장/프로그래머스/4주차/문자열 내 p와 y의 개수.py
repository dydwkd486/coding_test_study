from collections import Counter
def solution(s):
    a= Counter(s.upper())
    if a['Y']==a['P']:
        return True
    else:
        return False

def solution(s):
    y=0
    p=0
    for i in s.upper():
        if i=="Y":
            y+=1
        if i=="P":
            p+=1
    
    return y==p

def solution(s):
    return s.upper().count('Y')==s.upper().count('P')
