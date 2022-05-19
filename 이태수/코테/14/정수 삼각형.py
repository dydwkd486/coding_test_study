
def solution(triangle):
    a = []
    for i, v in enumerate(triangle):
        for i2, v2 in enumerate(v):
            if i2 == 0 and i != 0:
                triangle[i][i2] = v2+triangle[i-1][0]
            elif i2 == len(v)-1 and i != 0:
                triangle[i][i2] = v2+triangle[i-1][i2-1]
            elif i != 0:
                 triangle[i][i2] = max(v2+triangle[i-1][i2-1],v2+triangle[i-1][i2])

    return max(triangle[i])

"""
7
0

38
01

810
012

2744
0123

45265

"""