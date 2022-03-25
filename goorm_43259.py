import re
def sparta():
    string = str(input())
    string = re.sub(" ","",string)
    print(string)
sparta()

# def sparta2():
#     a=input().replace(' ','')
#     print(a)
# sparta2()

def sparta3():
    a = input(str.maketrans(" ",''))
    print(a)
