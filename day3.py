# Write a function to count the number of vowels in a given string 

def count_vowel(s):
  lower_s=s.lower()
  count=0
  for c in lower_s:
    if c in "aeiou":
      count+=1
  return count

s=input("Please input a phrase/word:")
vowel_num=count_vowel(s)
print(f"The phrase/word {s} has {vowel_num} vowel(s).")