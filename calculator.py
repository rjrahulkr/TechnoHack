class Calculator:
    def add(self, x, y):
        """Addition"""
        return x + y

    def subtract(self, x, y):
        """Subtraction"""
        return x - y

    def multiply(self, x, y):
        """Multiplication"""
        return x * y

    def divide(self, x, y):
        """Division"""
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

    def power(self, x, y):
        """Exponentiation"""
        return x ** y

    def factorial(self, x):
        """Factorial"""
        if x < 0:
            return "Factorial is not defined for negative numbers"
        elif x == 0:
            return 1
        else:
            return x * self.factorial(x - 1)

    def gcd(self, x, y):
        """Greatest Common Divisor"""
        while y != 0:
            x, y = y, x % y
        return x

    def lcm(self, x, y):
        """Least Common Multiple"""
        return abs(x * y) // self.gcd(x, y)

# Create an instance of the Calculator class
calculator = Calculator()

# Main program loop
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Factorial")
    print("7. Greatest Common Divisor")
    print("8. Least Common Multiple")
    print("0. Exit")

    choice = input("Enter choice (0-8): ")

    if choice == '0':
        print("Exiting the calculator.")
        break

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", calculator.add(num1, num2))

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", calculator.subtract(num1, num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", calculator.multiply(num1, num2))

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", calculator.divide(num1, num2))

        elif choice == '5':
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter exponent: "))
            print("Result:", calculator.power(num1, num2))

        elif choice == '6':
            num = int(input("Enter a number: "))
            print("Result:", calculator.factorial(num))

        elif choice == '7':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Result:", calculator.gcd(num1, num2))

        elif choice == '8':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Result:", calculator.lcm(num1, num2))

    else:
        print("Invalid Input")
