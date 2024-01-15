# Write a program to find the sum of all elements in a list.

while True:
  try:
    num_str=input("Enter numbers separated by spaces: ")
    list=list(map(int, num_str.split()))
    result=sum(list)
    print(f"The sum of the {list} is: {result}.")
    break
  except ValueError:
    print("Only numbers separated by spaces are accepted.")