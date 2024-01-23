# Write a program to shuffle the elements of a list randomly.
from random import shuffle

def shuffle_list(arr):
  shuffle(arr)
  return arr

str=input("Input entries separated by spaces: ")
arr=str.split(" ")
shuffled = shuffle_list(arr)
print(f"After shuffle: {shuffled}")