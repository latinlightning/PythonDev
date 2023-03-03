#ask for age
age = input("How Old Are You? \n")

# 18 to 21 wristband
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband")
    elif age >= 21:
        print("You are good to enter and can drink!")
    else:
        print("Too young Go away!")
else: 
    print("Enter an Age")