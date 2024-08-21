NameOne = input("Enter Name: ")
NameTwo = input("Enter Name: ")
NameThree = input("Enter Name: ")
result = ("Your Classmates are: " + NameOne + ", " + NameTwo + " & " + NameThree)
print(result)
FirstNumber = int(input("Enter Number One: "))
SecondNumber = int(input("Enter Number Two: "))
if FirstNumber < SecondNumber:
    print(str(FirstNumber) + " is Less than " + str(SecondNumber))
elif FirstNumber > SecondNumber:
    print(str(FirstNumber)+ " is Greater Than " + str(SecondNumber))
else:
    print(str(FirstNumber) + " is Equal to " + str(SecondNumber))