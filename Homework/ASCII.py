ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly ONE character.")
else:
    print("You entered:", ch)
    print("ASCII value:", ord(ch))