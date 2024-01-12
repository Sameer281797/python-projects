sum = 0
while(True):
    userinput = input("Enter the item price or press q to quit :\n")

    if(userinput!= 'q'):
        sum = sum + int(userinput)
        print(f"order total soo far : {sum}")
        
    else:
        print(f"Your total bill is {sum} Rs. Thanks for shopping with us!")
        print("Visit again!")
        break
