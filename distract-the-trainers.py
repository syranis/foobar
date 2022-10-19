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
                # This while loop never ends for 1, 2 and multiples even though it repeats all the time
                # essentially, TODO: stop being a dunce you bellend
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
                previous.add((smaller, bigger))
            del bigger, smaller
    return infinites


infinites = solution([1, 7, 3, 21, 13, 19])
print(infinites)
for i in infinites:
    print(len(infinites[1]))
