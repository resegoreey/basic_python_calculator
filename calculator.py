#function for addition
def add(num1, num2):
  return num1 + num2

#function for subtraction 
def subtr(num1, num2):
  return num1 - num2

#function for multiplication 
def multiply(num1, num2):
  return num1 * num2

#function for division 
def divide(num1, num2):
  if num2 != 0:
    return num1 / num2
  else:
    print("You cannot divide by zero!")


def calculator():

  while True:

   try:
    #prompt the user for input 
    user_input = input("Choose the operation you want to use (+. -, *, /): ")
    num1 = float(input("first number?: "))
    num2 = float(input("second number?: "))

  #perform the calculations based on the operator 
    if user_input == "+":
        result = add(num1, num2)
        print(f"results: {round(result, 1)}")

    elif user_input == "-":
        result = subtr(num1, num2)
        print(f"results: {round(result, 1)}")

    elif user_input == "*":
        result = multiply(num1, num2)
        print(f"results: {round(result, 1)}")

    elif user_input == "/":
    #handle division by zero 
      If num2 == 0
        raise ZeroDivisionError("Cannot divide by zero")
      result = divide(num1, num2)
      print(f"results: {result }")
    else:
      #Invalid operator 
        raise ValueError(f"{user_input} is a/n Invalid Option!")
   except ValueError as ve:
     print(f"Input error: {ve}") 
   except ZeroDivisionError as zde:
     print(f"Math Error: {zde}")

#asking the user if they want to continue or exit

    user_decision = input("Do you want to continue with your calculations? ").lower()
    if user_decision != "yes":
      print("Exiting the calculator, Bye bye!")
      break
    
#running the calculator 
calculator()
