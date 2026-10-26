import sys

sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")


num = int(input( ))
if num < 0:
    print( "the number is negative")
elif num > 0:
    print( "the number is positive")
else:
    print("the number is zero")
