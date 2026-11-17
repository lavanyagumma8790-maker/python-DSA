arr = [1,3,5,7,11,13,15]
target = 13
for index,value in enumerate(arr):
    if value == target:
        print("element is found at index",index)
        break
else:
    print("element is not found")
        