#write a number to perform a sum of digits in a user defined number
'''num = int(input("Enter a number: "))
sum = 0
while num != 0:
    digit = num % 10
    sum += digit
    num = num//10
print("Sum of digits : ", sum) '''
#write a code to perform reverse of a user-defined number
num = int(input("Enter a number: "))
rev = 0
while num !=0:
    digit = num % 10
    rev = (rev*10)+digit
    num = num//10
print("Reversed number: ", rev)
#write a code to perform a palindromic number
num = int(input("Enter a number: "))
temp = num
rev=0
while num !=0:
    digit = num % 10
    rev = (rev*10)+digit
    num=num//10
if temp==rev:
    print(rev, "is a palindrome")
else:
    print(rev, "is not palindrome")