'''
ex.5
Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse.
For example, 545, is the palindrome numbers
DO NOT use reverse builtin function.

'''
number = int(input("Enter a number: "))
original_number = str(number)
if original_number == original_number[::-1]:
    print(f"{original_number} is a palindrome number.")
else:
    print(f"{original_number} isn't a palindrome number.")
