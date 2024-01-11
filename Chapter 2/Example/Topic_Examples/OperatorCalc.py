# Build A Calculator Using Match Case (switch case in java);

num1 = int(input("Enter First Number : "))
operator = input("Enter The Operator : ")
num2 = int(input("Enter Second Number : "))

# match case 

match (operator) :
    case "+" :
        print("The Sum Is : ", num1 + num2)
    case "-" :
        print("The Differance Is : ", num1 - num2)
    case "*" :
        print("The Multiplication Is : ", num1 * num2)
    case "/" :
        print("The Division Is : ", num1 / num2)
    case "%" :
        print("The Modulus Is : ", num1 % num2)
    case _ :
        print("Please Enter A Valid Operator 😒")   # "Default Case "