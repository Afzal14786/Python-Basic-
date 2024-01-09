name = "Md Afzal Ansari"
age = 20
address = "Mumbai Maharashtra"

# print("My Name Is : " + name + "\n" + "My Age Is : " + age +" My Address Is : " + address)
'''
    Error We Got :-
        print("My Name Is : " + name + "\n" + "My Age Is : " + age +" My Address Is : " + address)
TypeError: can only concatenate "str" "(not "int") to str"
'''

'''
# Soultion #

    We Can Use Comma(,) Instant Of + Sign 
'''
print("My Name Is : " + name +"\n" +"My Address Is : " + address + "\n" +  "My Age Is : ", age )

