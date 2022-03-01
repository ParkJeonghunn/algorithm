h,m = map(int, (input().split(" ")))
0<=h<=23, 0<=m<=59

if h >=1 and m>=45:
    print(h, m-45)
elif h >=1:
    print(h-1, 60-(45-m))
elif h ==0 and m>=45:
    print(h, m-45)
else:
    print(23, 60-(45-m))
    
