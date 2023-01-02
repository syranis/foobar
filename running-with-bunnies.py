import itertools


def solution(times, time_limit):
    # initialize
    length = len(times)
    previous = [[None] * length] * length
    shortest_times = [[0] * length] * length

    # find the shortest path from each node to all other nodes (and check the graph for negative cycles)
    for i in range(length):
        shortest_times[i], previous[i] = shortestSingleSource(times, i)
        if cycleDetection(times, shortest_times[i]):
            return list(range(length - 2))

    # brute force
    best_try = []
    for i in list(powerset(length - 1)):
        for combo in list(itertools.permutations(i)):
            combo = list(combo)
            combo.insert(0, 0)
            combo.append(length - 1)
            path_length = 0

            for edge_origin in range(len(combo) - 1):
                path_length += shortest_times[combo[edge_origin]][combo[edge_origin + 1]]

            if path_length <= time_limit and len(combo) > len(best_try):
                best_try = combo

    # bunnies only
    answer = set()
    for edge_origin in range(len(best_try) - 1):
        answer.update(backtrack(best_try[edge_origin], best_try[edge_origin + 1], previous))

    return [x - 1 for x in sorted(list(answer))[1:-1]]


def powerset(num_bunnies):
    s = list(range(1, num_bunnies))
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1, num_bunnies + 1))


def shortestSingleSource(times, origin):
    # initialization
    length = len(times)
    cost_estimates = [float('inf')] * length
    previous = [None] * length
    cost_estimates[origin] = 0

    # relaxation
    for i in range(length - 1):
        for u in range(length):
            for v in range(length):
                if cost_estimates[u] + times[u][v] < cost_estimates[v]:
                    cost_estimates[v] = cost_estimates[u] + times[u][v]
                    previous[v] = u
    return cost_estimates, previous


def cycleDetection(times, time_slice):
    length = len(times)
    for u in range(length):
        for v in range(length):
            if time_slice[u] + times[u][v] < time_slice[v]:
                return True
    return False


def backtrack(origin, destination, previous):
    visited = {origin, destination}
    current = previous[destination][origin]
    while current and current != origin:
        visited.add(current)
        current = previous[destination][current]
    return visited
