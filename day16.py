# Write a function that counts the frequency of each word in a str.

def frequency(str):
  freq_dict = {}
  for char in str:
      if char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' or char==" ":
          continue
      if char in freq_dict:
          freq_dict[char] += 1
      else:
          freq_dict[char] = 1

  return freq_dict

str=input("Enter a str: ")
print(f"{frequency(str)}")