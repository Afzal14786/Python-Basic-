# Take Positive Integer input and tell if it is divisible by 5 or 3 but not divisible by 15

num = int(input("Enter The Number : "))

if (num % 15 == 0) :
    print("The Number Is Divisible By 15 .")
else :
    if (num % 3 == 0 or num % 5 == 0) :
        print("The Number Is Not Divisible By 15 But Divisible By 3 or 5")
    else :
        print("Neither Divisible By 3 Nor By 5")