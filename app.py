details = input("Enter P if (Proceed) E for (Exit) ")
while details == "P":
        if details == "p":
            print("Invalid Key")
        num1 = int(input("Enter Number One: "))
        num2 = int(input("Enter Number Two: "))
        if num1 < num2:
            print(f"{num1} is Less than to {num2}")
        elif num1 > num2:
            print(f"{num1} is Greater than to {num2}")
        else:
            print(f"{num1} and {num2} are Both Equal")
        details = input("Enter P if (Proceed) E for (Exit)")

if details == "E":
    print("Program Exit")
else:
    print("Invalid Key")

