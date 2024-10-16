# Function for addition
def add(num1, num2):
    return num1 + num2

# Function for subtraction 
def subtr(num1, num2):
    return num1 - num2

# Function for multiplication 
def multiply(num1, num2):
    return num1 * num2

# Function for division 
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("You cannot divide by zero!")

def calculator():
    while True:
        try:
            # Prompt the user for input 
            user_input = input("Choose the operation you want to use (+, -, *, /): ")
            num1 = float(input("First number?: "))
            num2 = float(input("Second number?: "))

            # Perform the calculations based on the operator 
            if user_input == "+":
                result = add(num1, num2)
                print(f"Result: {round(result, 1)}")

            elif user_input == "-":
                result = subtr(num1, num2)
                print(f"Result: {round(result, 1)}")

            elif user_input == "*":
                result = multiply(num1, num2)
                print(f"Result: {round(result, 1)}")

            elif user_input == "/":
                result = divide(num1, num2)
                if result is not None:  # Ensure there's no division by zero
                    print(f"Result: {round(result, 1)}")
            else:
                # Invalid operator 
                raise ValueError(f"{user_input} is an invalid option!")
        except ValueError as ve:
            print(f"Input error: {ve}") 
        except ZeroDivisionError as zde:
            print(f"Math Error: {zde}")

        # Asking the user if they want to continue or exit
        user_decision = input("Do you want to continue with your calculations? (yes/no): ").lower()
        if user_decision != "yes":
            print("Exiting the calculator, Bye bye!")
            break

# Running the calculator 
#calculator()
