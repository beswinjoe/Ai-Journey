exp = []

print("Welcome to the Daily Expense Tracker!\n")

while True:
    print("\nMenu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")

    try:
        a = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if a == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    elif a == 1:
        try:
            b = float(input("Enter expense amount: "))
            exp.append(b)
            print("Expense added successfully!")
        except ValueError:
            print("Invalid amount.")

    elif a == 2:
        if not exp:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i, amt in enumerate(exp, start=1):
                print(f"{i}. {amt}")

    elif a == 3:
        if not exp:
            print("No expenses recorded yet.")
        else:
            tot = sum(exp)
            avg = tot / len(exp)
            print(f"Total expense: {tot}")
            print(f"Average expense: {avg}")

    elif a == 4:
        exp.clear()
        print("All expenses cleared.")

    else:
        print("Invalid choice. Try again.")
