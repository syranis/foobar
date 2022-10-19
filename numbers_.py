def solution(l, t):
    for start_ind in range(len(l)):
        conc = l[start_ind:]
        for end_ind in range(1, len(conc) + 1):
            if sum(conc[:end_ind]) == t:
                return start_ind, end_ind + start_ind - 1
    return -1, -1


print(solution([4, 3, 10, 2, 8], 12))