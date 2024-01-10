''' "For Taking Input In Python We Use Input Method " .
    Syntax : input()
    * We Can Also Add Statements Inside The Input Method.
        e.g : input("Enter Your Name : ")
    * Whatever We Take Input From The User, By Default It's Consider As A String Data Type .
# 
    * If We Take An Integer input Then It Will Consider As String Because It Will Automatically Consider As String .

    Exmples :
'''

# name = input("Enter Your Name : " )
# age = input("Enter Your Age : ")
'''Here If Both The Age And The Name Is Printed In The Same Line , It Mean's The Age Is Automatically Consider As String .
'''
# print("Your Name Is : " + name, "And Your Age Is : " + age)
# Here Age Is The String Not The Integer .

# roll_no = int(input("Enter Your Roll No : "))  # TypeCasting
# print("Your Roll No Is : " ,roll_no)

# Take Input Of Two Numbers And Sum It 

# first_num = int(input("Enter The First Number : "))
# second_num = int(input("Enter The Second Number : "))
# sum = first_num + second_num

# print("The Sum Of Two Number's Is : " , sum)

#----------------Arithmatic Operator's--------------------------

'''
        * The Arithmatic Operator's*
    '+' -> Addition Operator
    '-' -> Subtractor Operator
    '*' -> Multiplication Operators
    '/' -> Divide Operator
    '//' -> Floor Division {It Will Give The Nearest Whole Number}
    '**' -> Exponentation
    '%' -> Modulus {It Will Give The Reminder Of The Divison}
'''
# print("Division : ", first_num / second_num)
# print("The Floor Division Value Is : ", first_num // second_num)
# print("The Modulus Of The Entered Number : ", first_num % second_num)
# print("The Exponentiation Value Of Entered Number : ", first_num ** second_num)

#----------------Assignment Operator--------------------------

'''
        * Assignment Operators *
    # Operators     # Examples
    1. '='          n1 = n2
    2. '+='         n1 += n2 (n1 = n1 + n2)
    3. '-='         n1 -= n2 (n1 = n1 - n2)
    4. '/='         n1 /= n2 (n1 = n1 / n2)
    5. '//='        n1 //= n2 (n1 = n1 // n2)
    6. '**='        n1 **= n2   (n1 = n1 ** n2)
    7. '%='         n1 %= n2 (n1 = n1 % n2)
    8. '&='         n1 &= n2 (n1 = n1 & n2)
    9. '|='         n1 |= n2 (n1 = n1 | n2)
    10. '^='        n1 ^= n2 (n1 = n1 ^ n2)
    11. '>>='       n1 >>= n2  (n1 = n1 >> n2)
    12. '<<='       n1 <<= n2  (n1 = n1 << n2)
'''
n1 = 10
n2 = 10

# print(n1, n2)
# n1 += n2 # n1 is updated (n1 = n1 + n2)
# n2 = n1 + n2    # Here n2 Is Updated (n2 += n1)
# print(n1, n2)


#----------------Comparison Operator--------------------------
'''
    * Comparison Operator *
    * These Operators Only Give Boolean Output : True or False

    Operator            Name
    '=='               Equal too
    '!='               Not Equaltoo
    '>'                Greater Than
    '<'                Less Than
    '>='               Greater Than Equaltoo
    '<='               Lessthan Equal Too

    Examples : 
'''
'''
print("Is Both Numbers Are Equal : ", first_num == second_num)
print("Is Both Are Not Equal : ", first_num != second_num)
print("Is First Is Greater Than Second : ", first_num > second_num)
print("Is First Is Less Than Second : ", first_num < second_num)
print("Is First Is Equla Or Greater Than Second : ", first_num >= second_num)
print("Is First Is Lessthan Or Equal Too The Second : ", first_num <= second_num)
'''


#----------------Logical Operator----------------------------

'''
        * Logical Operator's *
        * Logical Operator Only Work With Boolean Values .
    
    Operators               Name

    1. "and"           return true if both statements are True
    2. "or"            return true if any one statement is True
    3. "Not"           Reverse The Result, return false if the result is true

    example 1 : and (&) Operator

    Statement1          Statement2          Operators           Output
    True                False               and (&)             False
    False               True                and (&)             False
    False               False               and (&)             False
    True                True                and (&)             "True"

    example 2 : or (|) Operator

    Statement1          Statement2          Operators           Output
    True                False               or (|)             True
    False               True                or (|)             True
    False               False               or (|)             "False"
    True                True                or (|)             "True

    example 3 : not (!) Operator

    Statement1                Operators           Output
    True                      not (!)             False
    False                     not (!)             True

'''

stmt1 = 2 > 1   # True
stmt2 = 5 < 4   # False

print("And Operator Value :", stmt1 and stmt2)  # False
print("Or Operator Value :", stmt1 or stmt2)    # True
print("Not Operator Value :", not(stmt1))       # False


#---------------Identity Operator--------------------------
'''
        Operator's                  Name

            is                  return "true", if the both variable are the same object .
            is not              return "true", of both the variable are not the same object .
    
        Example : 
'''

# x = 6
# y = 6

# print("If X is Y ", x is y)
# print("If X is not Y ", x is not y)



#---------------Membership Operator--------------------------
'''
        Operator            Names

        in              return true if a sequence with the specified value "in" the object .
        not in          return true if a sequence with the specified value is "not in" the object .

    Examples :
'''

# friends_name = ["Afzal", "Faizal", "Rabbani", "Haider", "Firoz"]
# print("Is Friend Name Is Present In The Sequence : ", "Faizal" in friends_name)
# print("Friend That Are Not Present In The Sequence : ", "Faizal" not in friends_name)



#---------------Bitwise Operator--------------------------
'''         Operator                Name
               '&'                   "and"
               '|'                   "Or"
               '^'                   "XOR"
               '<<'                  "Left Shift"
               '>>'                  "Right Shift"
               '~'                   "Not"
'''

a = 5
b = 3
print("a and(&) b",a & b)
print("a or(|) b",a | b)
print("a XOR(^) b",a ^ b)
