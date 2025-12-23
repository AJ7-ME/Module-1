print("Welcome to the Birth Year Average Calculator!")
print("Please enter the birth years of your five friends.")
print("Please enter the year in YYYY format.\n")
one = int(input("Enter your first friend's birth year:\n "))
while one < 1900 or one > 2025:
    print("Please enter a valid year between 1900 and 2025.")
    one = int(input("Enter your first friend's birth year:\n "))
two = int(input("Enter your second friend's birth year:\n "))
while two < 1900 or two > 2025:
    print("Please enter a valid year between 1900 and 2025.")
    two = int(input("Enter your second friend's birth year:\n "))
three = int(input("Enter your third friend's birth year:\n "))
while three < 1900 or three > 2025:
    print("Please enter a valid year between 1900 and 2025.")
    three = int(input("Enter your third friend's birth year:\n "))
four = int(input("Enter your fourth friend's birth year:\n "))
while four < 1900 or four > 2025:
    print("Please enter a valid year between 1900 and 2025.")
    four = int(input("Enter your fourth friend's birth year:\n "))
five = int(input("Enter your fifth friend's birth year:\n "))
while five < 1900 or five > 2025:
    print("Please enter a valid year between 1900 and 2025.")
    five = int(input("Enter your fifth friend's birth year:\n "))
print("\nYour friends' birth years are:")
print(one)
print(two)
print(three)
print(four)
print(five)
average = (one + two + three + four + five) / 5
print("\nThe average birth year of your friends is:")
print(average)
year = 2025 - average
print("the average of all your friends age is:\n")
print(year)