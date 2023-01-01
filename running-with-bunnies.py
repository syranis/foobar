import itertools


def solution(times, time_limit):
    # find the shortest path from each node to all other nodes (and check for negative cycles)
    length = len(times)
    shortest_times = [[0] * length] * length
    for i in range(length):
        shortest_times[i] = shortestSingleSource(times, i)
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

            if path_length > time_limit or len(combo) <= len(best_try):
                continue
            best_try = combo

    # bunnies only
    answer = []
    for i in range(1, len(best_try) - 1):
        answer.append(best_try[i] - 1)

    return sorted(answer)


def powerset(num_bunnies):
    s = list(range(1, num_bunnies))
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1, num_bunnies + 1))


def shortestSingleSource(times, origin):
    # initialization
    length = len(times)
    cost_estimates = [float('inf')] * length
    cost_estimates[origin] = 0

    # relaxation
    for u in range(length):
        for v in range(length):
            if cost_estimates[u] + times[u][v] < cost_estimates[v]:
                cost_estimates[v] = cost_estimates[u] + times[u][v]
    return cost_estimates


def cycleDetection(times, time_slice):
    length = len(times)
    for u in range(length):
        for v in range(length):
            if time_slice[u] + times[u][v] < time_slice[v]:
                return True
    return False


print(solution([[0, 2, 2, 2, -1],
                [9, 0, 2, 2, -1],
                [9, 3, 0, 2, -1],
                [9, 3, 2, 0, -1],
                [9, 3, 2, 2, 0]], 1))
