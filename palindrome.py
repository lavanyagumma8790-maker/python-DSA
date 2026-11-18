a = 121
temp = a
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reversed number is:", rev)

if rev == a:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")