''' * Typecasing Is Something Where One Data Type Is Changed To The Another Data Type

example : integer to float
            float to integer
'''
Integernum1 = 12  # Integer
floatvalue = 99.76


# Here We Just Change The Data Type "int to float"
print("Int -> Float : ",float(Integernum1))

# Here We Just Change The Data Type "float To int"
print("Float -> Integer : ",int(floatvalue))

# We Can Also Change "int to string"
'''
Integer -> String :  12 And The Type Of The Integer Now : <class 'str'>
'''
num1 = str(Integernum1)
print("Integer -> String : ",str(Integernum1),"And The Type Of The Integer Now : ", type(num1))