import sys

sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

name = input("Enter your name: ")
print("Hello, " + name + "!")


