def ask_user():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        return ask_user()


def ask_fruit():
    fruits = input("Enter A for Apple and B for Banana: ")
    if fruits == "A":
        return "Apple"
    elif fruits == "B":
        return "Banana"
    else:
        return ask_fruit()


display = ask_user()
container = []
for i in range(display):
    container.append(ask_fruit())

if len(container) > 1:

    FinalResult = ", ".join(container[:-1]) + ", " + "and " + container[-1]

    print(f"You have {FinalResult} on your list.")
