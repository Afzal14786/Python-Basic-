# Print from 1 to 10 using while loop

# i = 0
# while i <= 10 :
#     print(i, "Hello Afzal")
#     i += 1

x = 5
y = 0

# while x >= 0 :
#     x -= 1
#     y += 1

#     if x == y :
#         continue
#     else :
#         print(x, y)

while x >= 0 :
    if x == y :
        break
    else :
        print(x,y)

    x -= 1
    y += 1