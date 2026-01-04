print("Enter your age: ")
age = input()
age = float(age)
if age < 10 and age > 0:
    print("You are younger than 10")
elif age > 20 and age < 130:
    print("You are older than 20")
elif age <=0:
    print("Please enter a valid age")
elif age >= 10 and age <= 20:
    print("You are", age, "years old so therefore you meet the criteria")