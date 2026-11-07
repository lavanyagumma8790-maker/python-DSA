s = "education"
cons = 0
for i in s:
    if i not in "aeiouAEIOU":
        cons+=1
print("consonants are:",cons)