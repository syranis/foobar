cache = {}


def solution_(n, last):
    global cache
    if (n, last) in cache:
        return cache[n, last]
    if last == 1:
        return 0
    solutions = 0
    for s in range(1, min(n + 1, last)):
        if n == s:
            solutions += 1
        else:
            solutions += solution_(n - s, s)
    cache[n, last] = solutions
    return solutions


# def solution__(n, last):
#     solutions = 0
#     if last == 1:
#         return 0
#     for s in range(n if n < last else last - 1, int((math.sqrt(8*n + 1) - 1) // 2 - 1), -1):
#         if n == s:
#             solutions += 1
#         else:
#             solutions += solution__(n - s, s)
#     return solutions


def solution(n):
    return solution_(n, n)
    # return 245 * math.exp(0.0755 * n)


import time

# 50 -> 3657
# 100 -> 444792
# 120 -> 2194431
for i in (3, 4, 5, 6, 7, 8, 9, 10, 50, 100, 120):
    start = time.time()
    print(f"{i}:", solution(i), time.time() - start)
# print(time.time()-start)
