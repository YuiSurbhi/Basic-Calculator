print("~~~~~~Welcome to the Basic Calculator~~~~~~")

# Display the menu of operations
print("Select the operation to perform : ");
print("1. Add");
print("2. Subtract");
print("3. Multiply");
print("4. Divide");

# Get user input for the operation
operation = input();

# Check which operation the user choose
if operation == "1":
    # Prompt user for two numbers and perform addition
    num1 = input("Enter the first number : ");
    num2 = input("Enter the second number : ");
    # Convert input to integer, perform addition, and show result
    print("The sum is : ", str(int(num1) + int(num2)));

elif operation == "2":
    # Prompt user for two numbers and perform substraction
    num1 = input("Enter the first number : ");
    num2 = input("Enter the second number : ");
    # Convert input to integer, perform substraction, and show result
    print("The difference is : ", str(int(num1) - int(num2)));

elif operation == "3":
    # Prompt user for two numbers and perform multiply
    num1 = input("Enter the first number : ");
    num2 = input("Enter the second number : ");
    # Convert input to integer, perform multiply, and show result
    print("The product is : ", str(int(num1) * int(num2)));

elif operation == "4":
    # Prompt user for two numbers and perform divide
    num1 = input("Enter the first number : ");
    num2 = input("Enter the second number : ");
    # Convert input to integer, perform divide, and show result
    # Note: This code does not handle division by zero errors
    print("The result is : ", str(int(num1) / int(num2)));

else:
    # Handle invalide operation entry
    print("invalid entry.");