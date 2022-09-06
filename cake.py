def solutiona(s):
    previous = s
    while True:
        for letter in range(1, len(previous)):
            print(previous[:letter])
            print(previous[letter:len(previous[:letter]) + letter])
            if previous[:letter] == previous[letter:len(previous[:letter]) + letter]:
                pattern = previous[:letter]
        try:
            if previous == pattern:
                break
        except UnboundLocalError:
            pattern = s
            break
        previous = pattern

    return s.count(pattern)


def solution(s):
    for ind in range(1, len(s) + 1):
        if len(s) % ind == 0 and s[:ind] * (len(s) // ind) == s:
            return len(s) // ind


print((solution('abcab')))