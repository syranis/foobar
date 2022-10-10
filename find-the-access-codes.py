def solution(l):
    triples = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                for k in range(j + 1, len(l)):
                    if l[k] % l[j] == 0:
                        triples += 1
    return triples


assert solution([1, 1, 1]) == 1
assert solution([1, 2, 3, 4, 5, 6])
