m, n = input().split()
def snake():
    if int(m) >=3 and int(n) >=3 and int(m) <= 100 and int(n) <= 100:
        print('*' * int(m))
        for i in range(1, int(n)):
            if n == 3:
                print('  ''*')
            elif n%4 == 1:
                print('*',''*int(m))
            elif n%4 == 3:
                print('  '*int(m),'*')



snake()

