def sortDecroissant(a, b):
    if a == b:
        return 0, 0
    if a > b:
        return a, b
    return b, a


def findLoops(list):
    infinites = {}
    for first in list:
        infinites[first] = []
        for second in list:
            previous = set()
            bigger, smaller = first, second
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
    for first in sorted(loops.keys(), key=lambda x: len(loops[x])):
        loops[first] = sorted(loops[first], key=lambda x: len(loops[x]))
        if len(loops[first]) == 0:
            continue
        final -= 2
        second = loops[first][0]
        for i in loops[first]:
            loops[i].remove(first)
        for i in loops[second]:
            loops[i].remove(second)
        loops[second] = []
    return final


print(solution([1, 3, 7, 13, 19, 21]))
