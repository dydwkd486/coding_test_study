def solution(sizes):
    a=0
    b=0
    for i in sizes:
        a = max(a, min(i))
        b = max(b, max(i))

    return a*b