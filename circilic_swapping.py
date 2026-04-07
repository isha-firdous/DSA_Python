#code to swap 3 numbers
a,b,c = map(int,input("Enter 3 numbers").split())
a = a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)
#res = a,b,c
print(f"numbers after swapping are: {a,b,c}")

