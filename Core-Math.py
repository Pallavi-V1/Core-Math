history = []

def calculator():
    while True:
        print("\n===== CORE MATH CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Power")
        print("7. View History")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "8":
            print("Thank you for using Smart Calculator!")
            break

        if choice == "7":
            if history:
                for item in history:
                    print(item)
            else:
                print("No calculations yet.")
            continue

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice!")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = a + b
                symbol = "+"
            elif choice == "2":
                result = a - b
                symbol = "-"
            elif choice == "3":
                result = a * b
                symbol = "*"
            elif choice == "4":
                if b == 0:
                    print("Cannot divide by zero!")
                    continue
                result = a / b
                symbol = "/"
            elif choice == "5":
                result = (a * b) / 100
                symbol = "% of"
            else:
                result = a ** b
                symbol = "**"

            message = f"{a} {symbol} {b} = {result}"
            print("Result:", result)
            history.append(message)

        except ValueError:
            print("Please enter valid numbers.")

calculator()
