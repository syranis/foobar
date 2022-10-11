def solution(l):
    cache = []
    triples = 0
    for j in range(1, len(l)):
        for k in range(j + 1, len(l)):
            if l[k] % l[j] == 0:
                cache.append({'j': [l[j], j], 'k': [l[k], k]})

    for i in range(len(l)):
        for double in cache:
            if double['j'][0] % l[i] == 0 and i not in (double['j'][1], double['k'][1]):
                triples += 1

    return triples


assert solution([1, 1, 1]) == 1
assert solution([1, 2, 3, 4, 5, 6]) == 3
