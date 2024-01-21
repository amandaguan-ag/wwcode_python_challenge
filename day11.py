# Write a program to print the multiplication table of a given number.


print("Welcome to the program to print the multiplication table of a given number")
while True:
  try:
    num = int(input("Input a number: "))
    for i in range(1,11):
      print(f"{num} * {i} = {num * i}")
  except ValueError:
    print("Please enter only integers.") 