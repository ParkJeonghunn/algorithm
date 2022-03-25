# a,b = input().split(' ')
# A = int(a)
# B = list(b)
# def repeat():
#     for i in B:
#         print(A*i,end='')
#
# repeat()

############################################

# a,b = input().split(' ')
# A = int(a)
# B = str(b)
# for i in B:
#     print(A*i)


#############################################
#
# n = int(input())
#
# for i in range(n):
#     a,b = input().split()
#     a = int(a)
#     b = str(b)
#     for i in range(len(b)):
#         print(a*b[i],end='')
#     print()

##############################################

# n = int(input())
#
# for i in range(n):
#     a,b = input().split()
#     a = int(a)
#     b = list(b)
#     for i in b:
#         print(a*i,end='')
#     print()

##############################################

# import random
#
# alphanumeroic = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'
# alpha = list(alphanumeroic)
#
# print(alpha)
#
# case_num = int(input())
# for i in range(case_num):
#     R = random.randint(1, 8)
#     len_S = random.randint(1,20)
#     S = random.sample(alpha, len_S)
#     print(R, S)
#     sum_S = ''
#     for j in range(len_S):
#         sum_S += S[j] * R
#
#     print(sum_S)