num = int(input())
Number = list(input())
def plus():
    sum = 0
    for i in range(num):
        sum += int(Number[i])
    return sum

print(plus())

# import sys
#
# n = int(sys.stdin.readline())
# num = list(sys.stdin.readline().rstrip())
# sum = 0
# for i in range(n):
#     sum += int(num[i])
# print(sum)