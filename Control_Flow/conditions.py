age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else :
    print("You are a minor.")


age = 20 
has_id = True
if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("No Entry")

score = 85
if score >= 90:
    print("Grade : A")
elif score >= 80:
    print("Grade : B")
elif score >= 70:
    print("Grade : C")
elif score >= 60:
    print("Grade : D")
else:
    print("Grade : F")

age = 20
status = "adult" if age >= 18 else "minor"
print(f"You are an {status}.")