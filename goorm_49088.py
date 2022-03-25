# import math
# def bros():
#     a, b = input().split()
#     c = input()
#     A = int(a)
#     B = int(b)
#     C = int(c)
#     if A >= 1 and B >= 1 and C <= 100:
#         for i in range(1,C+1):
#             total = A+B
#             if i % 2 ==1:
#                 A = math.floor(A/2)
#                 B = total - A
#             else:
#                 B = math.floor(B/2)
#                 A = total - B
#     return print(A,B)
#
# bros()

##################################################

# m, n = input().split()
# m = int(m)  # 형
# n = int(n)  # 동생
#
# d = int(input()) # 알고싶은날
#
# for i in range(1, d+1):
#     total = m + n
#     if i % 2 == 1:
#         m = round(m / 2)
#         n = total - m
#         # print(m,n)
#     else:
#         n = round(n / 2)
#         m = total - n
#         # print(m, n)
#
# print(m, n)

######################################################

# def good_brother():
#     jinwoo, sunwoo = input().split()
#     jinwoo = int(jinwoo)
#     sunwoo = int(sunwoo)
#     days = int(input())
#     for day in range(days):
#         if day % 2 == 0:
#             if jinwoo % 2 == 0:
#                 jinwoo = int(jinwoo/2)
#                 sunwoo = jinwoo + sunwoo
#             else:
#                 jinwoo = int(jinwoo//2)
#                 sunwoo = jinwoo + 1 + sunwoo
#         else:
#             if sunwoo % 2 == 0:
#                 sunwoo = int(sunwoo/2)
#                 jinwoo = sunwoo + jinwoo
#             else:
#                 sunwoo = int(sunwoo//2)
#                 jinwoo = sunwoo + 1 + jinwoo
#     return print(jinwoo, sunwoo)
# good_brother()

arr1 = [0 for i in range(5)]
print(arr1)