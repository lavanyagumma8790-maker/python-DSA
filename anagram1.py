a = "lavanya"
b = "aynaval"

freq = {}

# Count characters in first string
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Decrease characters in second string
for i in b:
    if i in freq:
        freq[i] -= 1
    else:
        freq[i] = -1

# Check frequencies
if all(value == 0 for value in freq.values()):
    print("Both strings are anagrams")
else:
    print("Strings are not anagrams")