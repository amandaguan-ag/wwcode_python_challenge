# Write a program to find the maximum and minimum values in a list.
while True:
  try:
    num_str=input("Enter numbers separated by spaces: ")
    list=list(map(int, num_str.split()))
    min, max= min(list), max(list)
    print(f"The minimum of {list} is: {min}, the maximum of {list} is {max}.")
  except ValueError:
    print("Only numbers separated by spaces are accepted.")