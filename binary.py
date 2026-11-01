arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 13

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if target == arr[mid]:
        print("Element is found")
        break

    elif target > arr[mid]:
        low = mid + 1

    else:
        high = mid - 1
else:
    print("Element is not found")