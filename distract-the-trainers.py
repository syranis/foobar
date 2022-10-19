def compareSize(a, b):
    if a == b:
        return 0, 0
    if a > b:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a
    return bigger, smaller


def solution(banana_list):
    infinites = {}
    for first in banana_list:
        infinites[first] = []
        for second in banana_list:
            previous = set()
            while True:
                try:
                    bigger, smaller = compareSize(bigger, smaller)
                    if (bigger, smaller) == (0, 0):
                        break
                except UnboundLocalError:
                    bigger, smaller = compareSize(first, second)
                if (bigger, smaller) in previous:
                    infinites[first].append((first, second))
                    break
                bigger -= smaller
                smaller *= 2
                previous.add((bigger, smaller))
            del bigger, smaller
    return infinites


print(solution([1, 2]))
