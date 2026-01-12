result=0.0
while True:

    print("==== Simple Calculator ====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reset")
    print("6. Exit")

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
