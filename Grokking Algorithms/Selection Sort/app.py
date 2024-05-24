def findSmallest(arr):
    smallest = arr[0] # stores the smallest value
    smallest_index = 0 #stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): #sorts an array
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr) #finds the smallest element in the array and adds it to the new array
        newArr.append(copiedArr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10])) 