# Write a program to count the occurrences of a specific character in a string.
str = input("Enter a string: ")
char = input("Enter a character: ")
count_char = str.count(char)

print(f"The character '{char}' occurs {count_char} time(s) in the string '{str}'.")