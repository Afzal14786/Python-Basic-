''' Print The Pattern
    1
    12
    123
    1234
'''

number = int(input("Enter The Number : "))

for i in range(1, number+1) :
    for j in range(1, i+1) :
        print(j, end=" ")
    print()
