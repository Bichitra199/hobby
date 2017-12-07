n=int(input("enter the number="))
factorial=1
if n<0:
    print("sorry factorial dosent exist for negative numbers")
else:
    for i in range(1,n+1,1):
        factorial=factorial*i
    print("the factorial for",n,"is",factorial)
