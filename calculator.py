def add(num1, num2):
  return num1 + num2

def subtr(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 != 0:
    return num1 / num2
  else:
    print("You cannot divide by zero!")


def calculator():
  
    user_input = input("Choose the operation you want to use (+. -, *, /): ")
    num1 = float(input("first number?: "))
    num2 = float(input("second number?: "))

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
        result = divide(num1, num2)
        print(f"results: {result }")
    else:
        print(f"{user_input} is a/n Invalid Option!")

calculator()
