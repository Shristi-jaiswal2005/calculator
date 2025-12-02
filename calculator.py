from demo import Calculator


def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def main() -> None:
    print("Simple Calculator")
    print("------------------")
    operations = {
        "1": ("Add", "add"),
        "2": ("Subtract", "subtract"),
        "3": ("Multiply", "multiply"),
        "4": ("Divide", "divide"),
        "5": ("Power", "power"),
        "6": ("Modulo", "modulo"),
    }

    while True:
        print("\nSelect operation:")
        for key, (label, _) in operations.items():
            print(f"{key}. {label}")
        print("Q. Quit")

        choice = input("Enter choice: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select a valid option.")
            continue

        num1 = read_number("Enter first number: ")
        num2 = read_number("Enter second number: ")

        calc = Calculator(num1, num2)
        _, method_name = operations[choice]
        method = getattr(calc, method_name)
        result = method()
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
