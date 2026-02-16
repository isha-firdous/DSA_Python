#write a code to find the negitive numbers in an array/list and replace
#them with zeros by traversal method
'''arr = list(map(int,input("enter elements in the array: ").split()))
print("array bfeore conversion: ",arr)
for i in range(len(arr)):
    if arr[i]<0:
        arr[i]=0
print("array is: ",arr)'''
#write a code to perform array reversal by 2 pointer approach and print the array
'''arr = list(map(int, input("Enter the numbers: ").split()))
left = 0
right = len(arr) - 1
while left < right:
    arr[left],arr[right] = arr[right],arr[left]
    left += 1
    right -= 1
print("reversed array: ",arr)'''
#write a code to consider string input from user and perform 
#replacement for all negative strings with 0/$
'''arr = input("enter elements in the array: ").split()
for i in range(len(arr)):
    if arr[i].startswith('-'):
        arr[i] = '$'
print("array is: ",arr)'''
#write a code to check if the given number is a palindromic number or not using 2 pointer approach.
num = input("enter the numbers: ")
left = 0
right = len(num)-1
is_palindrome = True
while  left < right:
    if num[left] != num[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
if is_palindrome:
    print("is a palindrome number")
else:
    print("is not a palindrome")
