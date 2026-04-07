#insertion sort create new index val nd move to the empty bucket
arr = list(map(int, input("Enter array values: ").split()))
n = len(arr)
print("Original array: ",arr)
for i in range(1, n):
    key = arr[i] #key=3
    j = i-1 #j=0
    while j >=0 and key < arr[j]:   #8>3 shift 8-> right 8>5 shift 8 3>2
        #8 8 5 2     
        arr[j+1]=arr[j]
        j -= 1
    arr[j+1] = key
print("Sorted array: ",arr)

#insertion sort create new index val nd move to the empty bucket