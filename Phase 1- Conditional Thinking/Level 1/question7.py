num1= int(input("enter first number: "))
print()
num2=int(input("enter second number: "))
print()
num3=int(input("enter third number: "))
print()

if( num1>num2 and num1 > num3):
    print("first number is large")
elif (num2 > num3):
    print("second number is large")
elif (num2 < num3):
    print(" third number is large")
else:
    print("the numbers are equal")