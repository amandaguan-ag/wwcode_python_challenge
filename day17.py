# Create a program that capitalizes the first letter of each word in a sentence

def capitalize_first_letter(str):
  words=str.split(" ")
  res=[]
  for word in words:
    if word:
      capitalized_word=word[0].upper()+word[1:]
      res.append(capitalized_word)
    else:
      res.append(word)
  return " ".join(res)

str=input("Enter a sentence: ")
print(f"After capitalizing the first letter: {capitalize_first_letter(str)}")