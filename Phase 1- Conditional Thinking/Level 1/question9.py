char= input("enter a character: ")
vowel = ['a','e','o','i','u']
if char.isalpha():  
    if char in vowel:
        print("the charcter is a vowel")
    else:
        print("the character is a consonant")
else:
    print("enter the valid character")