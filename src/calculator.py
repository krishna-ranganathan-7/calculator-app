result=0.0
while True:

    print("==== Simple Calculator ====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reset")
    print("6. Exit")
    print("===========================")

    choice = input("Choose an operation (1-6): ")

    if choice == "6":
        print("Exiting calculator.")
        break
    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
            continue
        if choice == "1":
            result = num1 + num2
            print("Result:", result)

        elif choice == "2":
            result = num1 - num2
            print("Result:", result)

        elif choice == "3":
            result = num1 * num2
            print("Result:", result)

        elif choice == "4":
            if num2 == 0:
                print("❌ Cannot divide by zero.")
                continue
            result = num1 / num2
        print("Result:", result)
        print("Current stored result:", result)
    elif choice == "5":
        result = 0
        print("🔄 Calculator reset. Result is now 0.")
    else:
        print("❌ Invalid choice. Please select only from 1 to 6.")
print("👋 Exiting calculator. Goodbye!")



