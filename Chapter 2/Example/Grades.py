# Take Input The Precentge and print the grades 
precentage = float(input("Enter The Precentage : "))

if (precentage > 80 and precentage <= 100) :
    print("Your Precentage Is ", precentage,"%", " : Very Good 👏")
elif (precentage > 60 and precentage <= 80) :
    print("Your Precentage Is ", precentage, "%", " : Good 👌")
elif (precentage > 40 and precentage <= 60) :
    print("Your Precentage Is ", precentage, "%", " : Average 👍")
else :
    print("Your Precentage Is ", precentage, "%", "Which Is Less Than 40, So Fail 😒")