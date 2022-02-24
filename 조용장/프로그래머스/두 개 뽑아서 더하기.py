from itertools import combinations
def solution(numbers):
    a = list(combinations(numbers,2))
    answer = []
    for i in a:
        answer.append(sum(i))
    return sorted(list(set(answer)))