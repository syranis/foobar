import pprint


def solution(times, time_limit):
    # find the shortest path from each node to all other nodes (and check for negative cycles)
    length = len(times)
    previous = [[None] * length] * length
    shortest_times = [[0] * length] * length
    for i in range(length):
        # TODO: Find a better way to do this
        try:
            shortest_times[i], previous[i] = shortestSingleSource(times, i)
        except TypeError:
            return list(range(length - 2))
    return


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


def backtrack(origin, destination, previous):
    visited = {origin, destination}
    current = previous[destination][origin]
    while current and current != origin:
        visited.add(current)
        current = previous[destination][current]
    return visited


pprint.pprint(solution([[0, 2, 2, 2, -1],
                        [9, 0, 2, 2, -1],
                        [9, 3, 0, 2, -1],
                        [9, 3, 2, 0, -1],
                        [9, 3, 2, 2, 0]], 0))
