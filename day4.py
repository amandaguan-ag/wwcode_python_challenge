# Write a program to find the sum of all elements in a list.

def sum_of_list(list):
  sum=0
  for num in list:
    sum+=num
  return sum

while True:
  try:
    num_str=input("Enter numbers separated by spaces: ")
    list=list(map(int, num_str.split()))
    result=sum_of_list(list)
    print(f"The sum of the {list} is: {result}.")
    break
  except ValueError:
    print("Only numbers separated by spaces are accepted.")