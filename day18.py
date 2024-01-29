# Create a program to find the largest among three numbers.

while True:
  try:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    num3=float(input("Enter the third number: "))
    print(f"The largest number is {max(num1,num2,num3)}")
  except ValueError:
    print("Please enter only number.") 