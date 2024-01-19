# Write a program to check if a number is even or odd.

def even_or_odd(num):
  if num % 2:
    return "odd"
  else:
    return "even"

while True:
  try:
    num=float(input("Enter a number:"))
    res=even_or_odd(num)
    print(f"Number {num} is {res}.")
  except ValueError:
    print("Please enter only numbers.")   