print("Enter marks obtained:")
m = float(input("Enter math marks: \n"))
if m < 0 or m > 100:
    print("Invalid marks entered.")
    exit()
s = float(input("Enter science marks: \n"))
if s < 0 or s > 100:
    print("Invalid marks entered.")
    exit()
e = float(input("Enter english marks: \n"))
if e < 0 or e > 100:
    print("Invalid marks entered.")
    exit()
ec = float(input("Enter economics marks: \n"))
if ec < 0 or ec > 100:
    print("Invalid marks entered.")
    exit()
g = float(input("Enter geography marks: \n"))
if g < 0 or g > 100:
    print("Invalid marks entered.")
    exit()
t = m + s + e + ec + g
av = t / 5
print("Your average marks are: ", av)
if av >= 91 and av <= 100:
    print("Congratulations! You are one of the toppers. You have secured A very good grade! Keep it up!")
elif av >= 81 and av <= 90:
    print("You have secured a quite good grade but there is little room for improvement! Keep it up!")
elif av >= 71 and av <= 80:
    print("You have secured an average grade and there is room for a small amount of room for improvement! Keep it up!")
elif av >= 61 and av <= 70:
    print("You have gotten a mid grade. You need to work hard to improve your performance.")
elif av >= 51 and av <= 60:
    print("You have secured a low grade. You need to work very hard to improve your performance.")
elif av <= 50 and av >= 40:
    print("You have secured a really low grade. You need to work extremely hard to improve your performance plus you are failing.")
elif av <= 39 and av >= 0:
    print("You have failed really badly. You need to repeat this class and work extremely hard to pass next time.")
else:
    print("Invalid marks entered.")