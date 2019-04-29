def findSmallest_index(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest_index(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr

print(selectionSort([4,6,2,7,12,8,1,56,123]))
