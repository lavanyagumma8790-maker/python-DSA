s = "swiss"
freq = {}
count = 0
for i in s:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1
print(freq)
for i in s:
    if freq[i] == 1:
        print("the first non-repeating character is:",i)
        break