def binary_search(arr, item):
    #low and high keep track of which part of the list you'll search in
    low = 0 
    high = len(arr)-1

    # While you haven't narrowed it down to one element...
    while low <= high:
        mid = (low + high) / 2 #check the middle element
        guess = arr[mid]
        # found the item
    if guess == item:
        return mid
    elif guess > item:
        high = mid - 1
    else:
        low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) 
print(binary_search(my_list, -1))