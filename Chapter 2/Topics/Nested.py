# Take 3 Number Input And Check Which One Is The Greates #
first_num = int(input("Enter The First Number : "))
second_num = int(input("Enter The Second Number : "))
third_num = int(input("Enter The Third Number : "))

if (first_num > second_num) :
    if (first_num > third_num) :
        print("First Number Is The Greatest Number", first_num)
    else :
        print("Third Number Is The Greates Number", third_num)
else :
    if (second_num > third_num) :
        print("Second Number Is The Greatest", second_num)
    else :
        print("Thirt Is The Greatest Number", third_num)