num = int(input("Enter a Number: "))
container = 0
container2 = []
for number in range(1, num +1):
    container += number 
    container2.append(str(number))

    result = ""
for number in range(len(container2)):
    result += container2[number]
    if number < len(container2) - 1:
        result += "+"
print(f"The result for {result} is {container}.")
