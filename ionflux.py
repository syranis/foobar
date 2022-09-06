import time


class node:
    def __init__(self, value, height, search, results):
        self.value = value
        if height > 1:
            leftval = value - pow(2, height - 1)
            rightval = value - 1

            for i in range(len(search)):
                if search[i] in (leftval, rightval):
                    results[i] = value

            self.left = node(leftval, height - 1, search, results)
            self.right = node(rightval, height - 1, search, results)

        else:
            self.left = None
            self.right = None

def build_tree(value, height, search, results):
    if height > 1:
        leftval = value - pow(2, height - 1)
        rightval = value - 1

        for i in range(len(search)):
            if search[i] in (leftval, rightval):
                results[i] = value

        build_tree(leftval, height - 1, search, results)
        build_tree(rightval, height - 1, search, results)

def solution(h, q):
    results = len(q) * [-1]
    start = time.time()
    build_tree(pow(2, h) - 1, h, q, results)
    print(time.time() - start)
    return results


print(solution(30, [7, 3, 5, 1]))