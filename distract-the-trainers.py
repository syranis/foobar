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
    used = []
    for first in sorted(loops.keys(), key=lambda x: len(loops[x])):
        if first in used:
            continue
        loops[first] = sorted(loops[first], key=lambda x: len(loops[x]))
        for second in loops[first]:
            if second not in used:
                used.extend([first, second])
                break
    return len(banana_list) - len(used)


print(solution([1, 7, 3, 21, 13, 19]))
