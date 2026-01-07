while True:
    ch = input("Enter a single character: \n")
    if len(ch) == 1:
        print("\nYou entered:", ch)
    else:
        print("\nInvalid input! You must enter ONE character.\n")
        continue
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        print(ch, "is an alphabet.\n")
    else:
        print(ch, "is not an alphabet.\n")