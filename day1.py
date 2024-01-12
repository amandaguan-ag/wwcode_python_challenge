# Create a program that swaps the values of two variables.
def swap(val1, val2):
  temp=val1
  val1=val2
  val2=temp
  return val1, val2

def main():
  print("Enter your first variable:")
  val1=input()
  print("Enter your second variable:")
  val2=input()
  print(f"Values:\n\tFirst variable:{val1}\n\tSecond variable:{val2}.")
  val1, val2=swap(val1,val2)
  print(f"Swapped values:\n\tFirst variable:{val1}\n\tSecond variable:{val2}.")
main()
