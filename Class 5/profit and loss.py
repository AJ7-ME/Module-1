cp = float(input("Enter the cost price: \n"))
sp = float(input("Enter the selling price: \n"))
if sp > cp:
    profit = sp - cp
    print(f"You made a profit of: \n${profit}")
if cp > sp: 
    Loss = cp - sp
    print(f"You incurred a loss of: \n${Loss}")