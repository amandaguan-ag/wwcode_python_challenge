# Write a program to print the first n numbers of a Fibonacci sequence

def first_n_fibonacci(n):
  fib_sequence=[]
  a,b=0,1
  for _ in range(n):
    fib_sequence.append(a)
    a,b=b,a+b
  return fib_sequence

while True:
  try:
    n=int(input("Enter how many numbers in a Fibonacci sequence:"))
    if n <= 0:
        print("Please enter a number greater than 0.")
    else:
      print(f"The first {n} numbers of a Fibonacci sequence: {first_n_fibonacci(n)}")
      break
  except ValueError:
    print("Please enter only integers.") 