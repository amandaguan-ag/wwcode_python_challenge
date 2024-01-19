# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def count_upper_and_lower(str):
  upper,lower=0,0
  for c in str:
    if c.isupper():
      upper+=1
    if c.islower():
      lower+=1
  return upper, lower

str = input("Enter a string:")
upper, lower = count_upper_and_lower(str)
print(f"Number of uppercase letter: {upper}")
print(f"Number of lowercase letter: {lower}")