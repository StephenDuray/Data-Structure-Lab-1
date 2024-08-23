print("----- AVERAGE GETTER SYSTEM -------")
sub1 = int(input("Enter Grade for Math: "))
sub2 = int(input("Enter Grade for English: "))
sub3 = int(input("Enter Grade for Science: "))
sub4 = int(input("Enter Grade for Filipino: "))
result = sub1 + sub2 + sub3 + sub4
average = result / int(4)
print("Your average is:", f"{average}")
if average >= 90:
    print("Execellent")
elif average >= 80:
    print("Very Good")
elif average >= 75:
    print("Not Bad")
else:
    print("Failed")
