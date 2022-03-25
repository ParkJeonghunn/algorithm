# match = 0
# n = int(input())
# while match < n-1:
#     match = match +1
#     print("%d번 경기를 했습니다." % match)
a = int(input())
def match():
    if a > 1:
        sum = 0
        for i in range(1, a):
         sum += i
        return print(sum)
    else:
        return
match()

