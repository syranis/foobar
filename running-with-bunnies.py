import pprint


def solution(times, time_limit):
    return allShortest(times)[0]


def shortestPath(times, origin):
    """
    Single source Bellman-Ford algorithm.
    Finds the shortest path to all other nodes from an origin node and their predecessor.
    """
    # Standard Dijkstra's initialization
    length = len(times)
    cost_estimates = [float('inf')] * length
    previous = [None] * length
    queue = list(range(length))
    cost_estimates[origin] = 0

    # Bellman-Ford relaxation
    for i in range(length - 1):
        for u in range(length):
            for v in range(length):
                if cost_estimates[u] + times[u][v] < cost_estimates[v]:
                    cost_estimates[v] = cost_estimates[u] + times[u][v]
                    previous[v] = u
    return cost_estimates, previous


def allShortest(times):
    # Get shortest
    length = len(times)
    previous = [[None] * length] * length
    shortest_times = [[0] * length] * length
    for i in range(length):
        shortest_times[i], previous[i] = shortestPath(times, i)
    return shortest_times, previous


pprint.pprint(solution([[0, 2, 2, 2, -1],
                        [9, 0, 2, 2, -1],
                        [9, 3, 0, 2, -1],
                        [9, 3, 2, 0, -1],
                        [9, 3, 2, 2, 0]], 0))
