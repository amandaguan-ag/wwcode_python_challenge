# Create a program that checks if a year is a leap year.

def leap_year(year):
  if year %100 != 0 and year % 4==0:
    return True
  elif year %100==0 and year %400==0:
    return True
  else:
    return False
while True:
  try:  
    year=int(input("Enter a year: "))
    if year <= 0:
        print("Please enter a year number greater than 0.")
    else:
      if leap_year(year):
        print(f"{year} is a leap year.")
      else:
        print(f"{year} is not a leap year.") 
  except ValueError:
    print("Please enter only integers.") 