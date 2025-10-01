n=int(input("enter a number: "))
temp=n
sum=0
digit=len(str(n))
while n>0:
    d=n%10
    sum=sum+(d**digit)
    n=n//10
if sum==temp:
    print("It is armstrong number")
else:
    print("It is not armstrong number")
