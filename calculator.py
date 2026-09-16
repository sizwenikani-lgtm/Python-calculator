# ==========================================
#  PYTHON CALCULATOR PROJECT
# ==========================================

history = []


def addition():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 + num2
    print("Answer:", answer)
    history.append(str(num1) + " + " + str(num2) + " = " + str(answer))


def subtraction():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 - num2
    print("Answer:", answer)
    history.append(str(num1) + " - " + str(num2) + " = " + str(answer))


def multiplication():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 * num2
    print("Answer:", answer)
    history.append(str(num1) + " * " + str(num2) + " = " + str(answer))


def division():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 == 0:
        print("Error: You cannot divide by zero.")
    else:
        answer = num1 / num2
        print("Answer:", answer)
        history.append(str(num1) + " / " + str(num2) + " = " + str(answer))


def remainder():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num2 == 0:
        print("Error: You cannot divide by zero.")
    else:
        answer = num1 % num2
        print("Remainder:", answer)
        history.append(str(num1) + " % " + str(num2) + " = " + str(answer))


def show_history():
    if len(history) == 0:
        print("There is no calculation history.")
    else:
        print("\n========== CALCULATION HISTORY ==========")
        for calculation in history:
            print(calculation)
        print("==========================================")


def clear_history():
    history.clear()
    print("Calculation history has been cleared.")


def main():
    while True:
        print("\n================================")
        print("       PYTHON CALCULATOR")
        print("================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Remainder")
        print("6. View History")
        print("7. Clear History")
        print("0. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                addition()
            except ValueError:
                print("Please enter numbers only.")
        elif choice == "2":
            try:
                subtraction()
            except ValueError:
                print("Please enter numbers only.")
        elif choice == "3":
            try:
                multiplication()
            except ValueError:
                print("Please enter numbers only.")
        elif choice == "4":
            try:
                division()
            except ValueError:
                print("Please enter numbers only.")
        elif choice == "5":
            try:
                remainder()
            except ValueError:
                print("Please enter whole numbers only.")
        elif choice == "6":
            show_history()
        elif choice == "7":
            clear_history()
        elif choice == "0":
            print("\nThank you for using the Python Calculator!")
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select an option from the menu.")


if __name__ == "__main__":
    main()
