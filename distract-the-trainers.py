def sortDecroissant(a, b):
    if a == b:
        return 0, 0
    if a > b:
        return a, b
    return b, a


def findLoops(list):
    infinites = {}
    for first in range(len(list)):
        infinites[first] = []
        for second in range(len(list)):
            if first == second:
                continue
            previous = set()
            bigger, smaller = list[first], list[second]
            while True:
                bigger, smaller = sortDecroissant(bigger, smaller)
                if (bigger, smaller) == (0, 0):
                    break
                if (bigger, smaller) in previous:
                    infinites[first].append(second)
                    break
                bigger -= smaller
                smaller *= 2
                previous.add((smaller, bigger))
    return infinites


def solution(banana_list):
    loops = findLoops(banana_list)
    final = len(banana_list)
    while loops:
        first = sorted(loops.keys(), key=lambda x: len(loops[x]))[0]
        loops[first] = sorted(loops[first], key=lambda x: len(loops[x]))
        if len(loops[first]) == 0:
            del loops[first]
            continue
        final -= 2
        second = loops[first][0]
        for i in loops[first]:
            loops[i].remove(first)
        for i in loops[second]:
            loops[i].remove(second)
        del loops[second]
        del loops[first]
    return final


print(solution([1]))
