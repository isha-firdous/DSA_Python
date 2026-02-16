#armstrong number/narscisstic,strong/krishnamurthy's number,harshd's/niven's number
#*Happy number*,atmorphic number,magic number
#write a code to check the given user-defined number is an armstrong number or not
'''num = int(input("Enter a number: "))
copy = num
sum = 0
while num!=0:
    digit = num % 10
    sum= sum+(digit**3)
    num= num // 10
if copy == sum:
    print(copy," is an armstrong number")
else:
    print(copy,"is not a armstrong number")'''
#if sum of a number is exactly divisible by the num then it is called harsh'd/niven number
#Niven/harshd number
'''num = int(input("Enter a number: "))
   copy = num
sum = 0
while num !=0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
if copy % sum == 0:
    print(copy, "is a Niven number")
else:
    print(copy, "is not a Niven number")'''
#stong number
num = int(input("Enter a number: "))
copy = num
sum = 0
while num !=0:
    digit = num % 10
    f=1
    i = 1
    while i<=digit:
        f=f*i
        i+=1
    sum = sum + f
    num = num // 10
if copy  == sum:
    print(copy, "is a strong number")
else:
    print(copy, "is not a strong number")