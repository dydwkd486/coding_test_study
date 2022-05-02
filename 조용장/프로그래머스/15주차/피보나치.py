dp = [0,1]
def fibo(n):
    for i in range(2,n+1):
        dp.append((dp[i-2]+dp[i-1])%1234567)
    answer = dp[-1]
    return answer

print(fibo(50))
print(dp)