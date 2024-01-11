# Take 3 Number Input And Check Which One Is The Greates #

first = int(input("Enter The First Number : "))
second = int(input("Enter The Second Number : "))
third = int(input("Enter The Third Number : "))

if (first > second and first > third) :
    print("First Number Is The Greatest", first)
elif (second > first and second > third) :
    print("Second Number Is The Greatest", second)
else :
    print("Third Number Is The Greatest", third)