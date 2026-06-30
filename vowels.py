text = input("Enter a word or sentence: ").lower()

count = 0

for char in text:
    if char in "aeiou":
        count += 1

print("Number of vowels =", count)