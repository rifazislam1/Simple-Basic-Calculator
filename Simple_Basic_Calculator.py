
def addition():
 try:
      a = float(input("Enter a number :"))
      b = float(input("Enter a number :"))
      print(f"The addition of two numbers is : {a+b}")
 except ValueError:
      print("Please enter a valid number.")

def multiplication():
 try:
      a = float(input("Enter a number :"))
      b = float(input("Enter a number :"))
      print(f"The multiplication of two numbers is : {a*b}")
 except ValueError:
      print("Please enter a valid number.")

def subtraction():
 try:
      a = float(input("Enter a number :"))
      b = float(input("Enter a number :"))
      print(f"The subtraction of two numbers is : {a-b}")
 except ValueError:
      print("Please enter a valid number.")

def division():
 try:
      a = float(input("Enter a number :"))
      b = float(input("Enter a number :"))
      if b == 0:
          print("Any number can not be divided by 0")
      else:
          print(f"The division of two numbers is : {a/b}")
 except ValueError:
      print("Please enter a valid number.")

operation = input("Choose an operation(+,-,*,/):")
if operation == "+":
    addition()
elif operation == "-":
    subtraction()
elif operation == "*":
    multiplication()
elif operation == "/":
    division()
else:
    print("The operation is invalid, thank you.")
 