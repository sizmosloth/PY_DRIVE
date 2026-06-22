# PRACTICE — A CALCULATOR THAT REFUSES TO CRASH


def calculator():
    while True:
        print("\n--- SAFE CALCULATOR ---")
        num1 = input("Enter first number (or 'q' to quit): ")

        if num1 == "q":
            print("Bye!")
            break

        try:
            num1 = float(num1)
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            else:
                raise ValueError("Invalid operator")

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Invalid input: {e}")
        except ZeroDivisionError:
            print("Can't divide by zero!")
        finally:
            print("Attempt finished.\n")

if __name__ == "__main__":
    calculator()