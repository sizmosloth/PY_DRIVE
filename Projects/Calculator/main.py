# A Calculator for operating multiple operands

def add (*args):
    sum = 0
    for i in args:
        sum += i
    print(f"The Sum is {sum}")

def sub (*args):
    sub = args[0]
    for i in args[1:]:
        if (i == 0):
            continue
        sub -= i
    print(f"The Subtraction is {sub}")
    
def prod (*args):
    prod = 1
    for i in args:
        prod *= i
    print(f"The Product is {prod}")

def main ():
    while True:
        print("---- CALCULATOR ----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. EXIT")

        choice = input("---- Enter your choice ---- : ")

        if choice == "1":
            arr = list(map(int, input("Enter Numbers: ").split()))
            add(*arr)
        elif choice == "2":
            arr = list(map(int, input("Enter Numbers: ").split()))
            sub(*arr)
        elif choice == "3":
            arr = list(map(int, input("Enter Numbers: ").split()))
            prod(*arr)
        elif choice == "4":
            print("bye!!!")
            break
        else:
            print("Invalid choice, try again !!!")
    
if __name__ == "__main__":
    main()
