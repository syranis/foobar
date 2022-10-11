import time


def solution(l):
    cache = {}
    triples = 0
    for j in range(1, len(l)):
        for k in range(j + 1, len(l)):
            if l[k] % l[j] == 0:
                cache[l[j]] = cache.get(l[j], 0) + 1

    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            if l[j] in cache and l[j] % l[i] == 0:
                triples += cache[l[j]]

    return triples


print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))


def badsolution(l):
    triples = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                for k in range(j + 1, len(l)):
                    if l[k] % l[j] == 0:
                        triples += 1
    return triples


def worsesolution(l):
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


def bestsolution(l):
    multiples = [[] for x in range(len(l))]
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                multiples[i].append(j)
    count = 0
    for j in range(len(l)):
        for k in multiples[j]:
            count += len(multiples[k])
    return count


l = list(range(1, 2000))
start = time.time()
print("solution: " + str(solution(l)))
print(time.time() - start)
start = time.time()
print("badsolution: " + str(badsolution(l)))
print(time.time() - start)
start = time.time()
print("worsesolution: " + str(worsesolution(l)))
print(time.time()-start)
start = time.time()
print("BESTsolution: " + str(bestsolution(l)))
print(time.time()-start)
