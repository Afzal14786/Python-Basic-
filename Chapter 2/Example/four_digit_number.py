# Check If The Number Is Four Digit Or Not #

number = int(input("Enter The Number : "))

if (number >= 1000 and number <= 9999) :
    print("It's A Four Digit Number : ", number)
else :
    print("It's Not A Four Digit Number :", number)