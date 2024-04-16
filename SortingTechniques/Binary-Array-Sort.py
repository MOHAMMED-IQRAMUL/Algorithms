arr = [0,1,0,1,1,1,0,1,1,1,1,1,0,1]

low = 0 
high = len(arr)-1

while low < high:
    
    while arr[low] == 0:
        low += 1

    while arr[high] == 1:
        high -= 1

    if low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
        
print(arr)

arr = [0,1,0,1,1,1,0,1,1,1,1,1,0]
