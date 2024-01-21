# Write a program to remove duplicates from a list.

def remove_duplicate(arr):
  res=[]
  for element in arr:
    if element in res:
      continue
    res.append(element)
  return res

# does not return original order
# def remove_duplicate(arr):
#   return list(set(arr))

str=input("Input entries separated by spaces: ")
arr=str.split(" ")
unique_list = remove_duplicate(arr)
print(f"The list without duplicates is {unique_list}.")
