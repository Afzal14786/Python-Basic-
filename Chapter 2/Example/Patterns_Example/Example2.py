# Print till the entered number 
# example if n = 5 then output = 12345 in five(5) rows

number = int(input("Enter The Number : "))

# Nested Loop #

for _ in range(number) :
    for i in range(1, number+1) :
        print(i, end="->")
    print() # for new line after one iteration 