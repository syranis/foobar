def xorn(number):
    if -2 < number % 4 - 2 < 1:
        final = '1'
    else:
        final = '0'
    for column in range(1, number.bit_length()):
        if (((number + 1) - ((number + 1) % (2 ** column))) // (2 ** column)) % 2 == 1 and \
                (number + 1) % (2 ** column) % 2 == 1:
            final = '1' + final
        else:
            final = '0' + final
    return int(final, 2)


# 0 1 2 /
# 3 4 / 5
# 6 / 7 8
# (0 -> 4) ^ ((0 -> 5) ^ (0 -> 4) ^ (0 ^ ) ^ (0 -> 6)

# 17 18 19 20 //
# 21 22 23 // 24
# 25 26 // 27 28
# 29 // 30 31 32
# (17 -> 23) ^ (17 -> 29) ^ (21 -> 24) ^ (25 -> 27)
def solution(start, length):
    checksum = xorn(start + length - 1) ^ xorn(start - 1)  # first line
    checksum ^= start + length ** 2 - length  # last line
    for line in range(1, length - 1):
        first = start + length * line - 1
        last = start + length * (line + 1) - line - 1
        print(f'{first} -> {last}')
        checksum ^= xorn(first) ^ xorn(last)
    return checksum


# c = 0
# for i in range(1, 65):
#     c ^= i
#     x = xorn(i)
#     print(f"{i=} xor={c} xor()={x} {c == x}")
#     if c != x:
#         print(f"expected {c:08b} = {c}")
#         print(f"got      {x:08b} = {x}")
#     assert c == x


print(solution(0, 3))
assert solution(0, 3) == 2
print(solution(17, 4))
assert solution(17, 4) == 14

# def solution_xor(start, length):
#     checksum = 0
#     for line in range(length):
#         for id in range(length - line):
#             checksum ^= start + length * line + id
#     return checksum
#
#
# def solution(start, length):
#     checksum = ''
#     for i in range(0, math.floor(math.log(start + length, 2)) + 1):
#         if i == 0:
#             checksum = str((start + length // 2) - (start - 1 // 2))
#         print(i)
#         divider = 2 ** i
#         result = ((start + length // divider + 1 * (divider // 2)) - (start - 1 // divider + 1 * (divider // 2))) % 2
#         if ((start + length // divider + 1) - (start - 1 // divider + 1)) % 2 == 1:
#             result += (start + length % divider - 3 ** (i - 1) + 1) - (start - length % divider - 3 ** (i - 1) + 1)
#         checksum = str(result) + checksum
#     return int(checksum, 2)
#
#
# print(solution(0, 3))
