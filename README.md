
Python Calculator with Error Handling

Overview

This is a simple command-line calculator implemented in Python that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. The calculator continuously prompts the user to perform calculations until they decide to exit. It also includes error handling to manage invalid inputs and prevent operations like division by zero.

Features

Basic Arithmetic Operations: Supports addition (+), subtraction (-), multiplication (*), and division (/).

Continuous Operation: The calculator runs in a loop, allowing the user to perform multiple calculations without restarting the program.

Error Handling: The calculator detects and handles:

Invalid numeric inputs.

Invalid operators.

Division by zero.


User-Friendly Interaction: After each calculation, the user is asked if they wish to continue or exit the program.



How to Use

1. Select an Operator: You will be asked to enter an operator from the following: +, -, *, or /.

2. Input the First Number: The calculator will prompt you to enter the first number.

3. Input the Second Number: After entering the firstnumber, provide the second number.

4. View the Result: The result of the calculation will be displayed.

5. Continue or Exit: After viewing the result, you will be asked if you want to perform another calculation. Type yes to continue or no to exit the program.



Example Run:

Enter an operator (+, -, *, /): +
Enter the first number: 12
Enter the second number: 5
Result: 12 + 5 = 17.0

Do you want to perform another calculation? (yes/no): yes

Error Handling

The calculator gracefully handles the following errors:

Invalid Number Input: If you enter a non-numeric value, you will be prompted to re-enter a valid number.

Enter the first number: abc
Input error: could not convert string to float: 'abc'

Invalid Operator: If you enter an operator that is not one of +, -, *, or /, an error message is displayed.

Enter an operator (+, -, *, /): %
Input error: Invalid operator! Please use +, -, *, or /.

Division by Zero: If you try to divide by zero, the program alerts you that division by zero is not allowed.

Enter the first number: 10
Enter an operator (+, -, *, /): /
Enter the second number: 0
Math error: Cannot divide by zero!


Code Explanation

The calculator is implemented using a while loop to keep the program running until the user decides to exit. It includes try-except blocks to catch and handle exceptions such as ValueError (for invalid input or operator) and ZeroDivisionError (for division by zero).

Here’s a brief overview of the code:

1. User Input: The user is asked to provide two numbers and an operator.


2. Arithmetic Operations: Based on the operator provided, the program performs the corresponding operation.


3. Error Handling:

If the user inputs a non-numeric value, the ValueError exception is caught.

If the user attempts to divide by zero, the ZeroDivisionError is caught.



4. User Decision: After each calculation, the user can choose to either perform another calculation or exit the program.
