'''
ex.2
Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.
'''

text = input("Input text: ")
while True:
  num = input("enter a number: ")
  if num.isdigit():
    if num > 0 or num = 0:
      print(text[num:])
      break
    else:
      print("Please enter a positive integer.")
  else:
    print("Invalid input. Please enter a valid number.")
