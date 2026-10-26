import sys

sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

num=int(input())

if (num%2 ==0):
    print("the number is even")
else:
    print("the number is odd")