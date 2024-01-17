# Write a program to check if a number is positive, negative, or zero.
def get_positivity(num):
  if num == 0:
    return "zero"
  elif num > 0:
    return "positive"
  else:
    return "negative"
  
while True:
  try:
    num=float(input("Enter a number:"))
    positivity=get_positivity(num)
    print(f"The number is {positivity}.")
  except ValueError:
    print("Please enter only numbers.")
