word = input("Enter a word or number: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")