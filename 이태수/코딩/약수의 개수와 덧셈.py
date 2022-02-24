def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if len(getMyDivisor(i))%2!=0:
            i *= -1
        answer +=i
    
    
    return answer