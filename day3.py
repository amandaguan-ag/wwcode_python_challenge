# Write a function to count the number of vowels in a given string 

def count_vowel(s):
  lower_s=s.lower()
  count=0
  for c in lower_s:
    if c in "aeiou":
      count+=1
  return count

s=input("Please input a word:")
vowel_num=count_vowel(s)
if vowel >1:
  print(f"It has {vowel_num} vowels.")
else:
  print(f"It has {vowel_num} vowel.")  