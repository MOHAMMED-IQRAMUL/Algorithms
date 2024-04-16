import time as T

def BubbleSort(Arr):
    for i in range(len(Arr)):
        flag = False 
        for j in range(len(Arr) - 1 - i):
            if Arr[j] > Arr[j + 1]:
                Arr[j], Arr[j + 1] = Arr[j + 1], Arr[j]
                flag = True
        if flag : break
    return Arr

def InsertionSort(Arr):
    for i in range(len(Arr)):
        j = i - 1
        x = Arr[i]
        while j >= 0 and Arr[j] > x:
            Arr[j + 1] = Arr[j]
            j -= 1
        Arr[j+1] = x
        
def SelectionSort(Arr):
    for i in range(len(Arr)-1):
        k = i
        for j in range(i, len(Arr)):
            if Arr[j] < Arr[k]:
                k = j
        Arr[i], Arr[k] = Arr[k], Arr[i]
        
def main1():
    Arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(Arr1)
    i1 = T.time()
    InsertionSort(Arr1)
    i2 = T.time()
    print(Arr1) 
    print(f"Time Taken is : {i2-i1}",end="\n\n")
    
    Arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(Arr2)
    i3 = T.time()
    InsertionSort(Arr2)
    i4 = T.time()
    print(Arr2)    
    print(f"Time Taken is : {i4-i3}",end="\n\n")


    Arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(Arr3)
    i5 = T.time()
    InsertionSort(Arr3)
    i6 = T.time()
    print(Arr3)  
    print(f"Time Taken is : {i5-i6}",end="\n\n")

main1()    

def main2():
    Arr1 = [9999,888,444,333,2222,777,555,44,33,22,111,222,333,444,55,66,77,9,98,7,6,5,4323456,78,76,54,3,456,7,6,54,34,567,8,765,432,345,67,87,654,3,456789,8,765,43,45,67,8,6543,23,456,78,76,543,2,345,67,87,65,432,3456,78,987,654,32,3,456,789,876,543,21,23,4567,89,87,654,32,34,567,89,876,543,2,345,678,7,6543,2,345,678,76,54,323,4567,89,87,6543,4567,89,876,5432,3,4567,89,87,6543,23,4567,89,87,6543,23,4567,89,876,54,1]
    print(Arr1)
    i1 = T.time()
    InsertionSort(Arr1)
    i2 = T.time()
    print(Arr1) 
    print(f"Time Taken is : {i2-i1}",end="\n\n")
    
    Arr2 = [9999,888,444,333,2222,777,555,44,33,22,111,222,333,444,55,66,77,9,98,7,6,5,4323456,78,76,54,3,456,7,6,54,34,567,8,765,432,345,67,87,654,3,456789,8,765,43,45,67,8,6543,23,456,78,76,543,2,345,67,87,65,432,3456,78,987,654,32,3,456,789,876,543,21,23,4567,89,87,654,32,34,567,89,876,543,2,345,678,7,6543,2,345,678,76,54,323,4567,89,87,6543,4567,89,876,5432,3,4567,89,87,6543,23,4567,89,87,6543,23,4567,89,876,54,1]
    print(Arr2)
    i3 = T.time()
    InsertionSort(Arr2)
    i4 = T.time()
    print(Arr2)    
    print(f"Time Taken is : {i4-i3}",end="\n\n")


    Arr3 = [9999,888,444,333,2222,777,555,44,33,22,111,222,333,444,55,66,77,9,98,7,6,5,4323456,78,76,54,3,456,7,6,54,34,567,8,765,432,345,67,87,654,3,456789,8,765,43,45,67,8,6543,23,456,78,76,543,2,345,67,87,65,432,3456,78,987,654,32,3,456,789,876,543,21,23,4567,89,87,654,32,34,567,89,876,543,2,345,678,7,6543,2,345,678,76,54,323,4567,89,87,6543,4567,89,876,5432,3,4567,89,87,6543,23,4567,89,87,6543,23,4567,89,876,54,1]
    print(Arr3)
    i5 = T.time()
    InsertionSort(Arr3)
    i6 = T.time()
    print(Arr3)  
    print(f"Time Taken is : {i5-i6}",end="\n\n")

# main2()      