# Create a program to calculate the area of a circle given its radius.

import math

def area_of_circle(r):
  return round(math.pi * r**2, 2)

while True:
  try:
    r=float(input("Enter radius:"))
    a=area_of_circle(r)
    print(f"Area of circle with radisu {r} is approximate to {a}")
    break
  except ValueError:
    print("Please enter a only numbers for the radius.")
