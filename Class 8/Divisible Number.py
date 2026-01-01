print("Enter a number(Numerator): \n")
n = int(input())
print("Enter a number(Denominator): \n")
d = int(input())
if n % d == 0:
    print("\n"+ str(n) + " is divisible by " + str(d))
else:
    print("\n"+ str(n) + " is not divisible by " + str(d))