import pprint


def solution(times, time_limit):
    length = len(times)
    previous = [[None] * length] * length
    shortest_times = [[0] * length] * length
    for i in range(length):
        try:
            shortest_times[i], previous[i] = shortestSingleSource(times, i)
        except TypeError:
            return list(range(length - 2))
    return shortest_times, previous


def shortestSingleSource(times, origin):
    # initialization
    length = len(times)
    cost_estimates = [float('inf')] * length
    previous = [None] * length
    cost_estimates[origin] = 0

    # relaxation
    for u in range(length):
        for v in range(length):
            if cost_estimates[u] + times[u][v] < cost_estimates[v]:
                cost_estimates[v] = cost_estimates[u] + times[u][v]
                previous[v] = u

    # negative cycle detection
    for u in range(length):
        for v in range(length):
            if cost_estimates[u] + times[u][v] < cost_estimates[v]:
                return True

    return cost_estimates, previous


pprint.pprint(solution([[0, 2, 2, 2, -1],
                        [9, 0, 2, 2, -1],
                        [9, 3, 0, 2, -1],
                        [9, 3, 2, 0, -1],
                        [9, 3, -1, 2, 0]], 0))
