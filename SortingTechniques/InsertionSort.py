def InsertionSort(Arr):
    for i in range(len(Arr)):
        j = i - 1
        x = Arr[i]
        while j >= 0 and Arr[j] > x:
            Arr[j + 1] = Arr[j]
            j -= 1
        Arr[j+1] = x