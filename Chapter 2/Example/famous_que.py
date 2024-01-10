# Find Out The Profit and Loss Of A Store 
product_price = int(input("Enter The Product Price : "))
selling_price = int(input("Enter The Selling Price : "))


# We Are Using The else if statement 
if selling_price > product_price :
    profit_amount = selling_price - product_price
    print("The Shopkeeper Makes Profit Of ", "₹", profit_amount)
elif (selling_price == product_price) : 
    print("The Shopkeeper Make Neither Loss Or Neither Profit")
elif  (selling_price < product_price) :
    loss_amount = product_price - selling_price
    print("The Shopkeeper Makes Loss Of ", "₹", loss_amount)
else :
    print("Customer LOL 🤣")