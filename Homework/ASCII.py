while True:
    ch = input("Enter a single character: ")

    if len(ch) != 1:
        print("Invalid input! Please enter exactly ONE character.\n")
        continue

    if type(ch) is not str:
        print("Invalid input! Input must be a string.\n")
        continue

    print("You entered:", ch)
    print("ASCII value:", ord(ch))

    if ch.isupper():
        print("Character type: Uppercase letter")
    elif ch.islower():
        print("Character type: Lowercase letter")
    elif ch.isdigit():
        print("Character type: Digit")
    else:
        print("Character type: Special character")

    break
