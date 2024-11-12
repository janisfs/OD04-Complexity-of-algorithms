# O(1) - константная сложность
def getElement(arr, index):
    return arr[index]

arr = [1, 2, 3, 4, 5]
print(getElement(arr, 2))


# O(n) - линейная сложность
def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
print(line_search(arr, 3))
print(line_search(arr, 6))


# O(log n) - логарифмическая сложность
def binary_search(arr, target):
    low, high = 0, len(arr)- 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(line_search(arr, 70))
print(line_search(arr, 25))