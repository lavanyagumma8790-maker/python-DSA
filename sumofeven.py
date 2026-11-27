arr = [12, 7, 8, 15, 20, 33, 44]
even = 0
sum =0

for i in arr:
    if i%2==0:
        even+=1
        sum+=i

    
print("even numbers are:",even)
print("sum of even elements:",sum)