

text = "Hello, World!"
countupper = 0
countlower = 0

for char in text:
    if char.isupper():
        countupper += 1
    elif char.islower():
        countlower +=1


print("Number of uppercase letters is ", countupper,"and Number of lowercase letters is ",countlower)
