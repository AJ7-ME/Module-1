while True:
    for i in range(3):
        character = input("Enter a character: \n")

        if len(character) != 1:
            print("Please enter exactly ONE character.")
        else:
            print("You entered:", character)
            print("Your ASCII value is:", ord(character))