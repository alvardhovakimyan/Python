'''
ex.9
write functions for the following string operations
is_in_str(str_obj, sub_string)

'''
def is_in_str(str_obj, sub_string):
    return sub_string in str_obj
string_obj = str(input("Enter your text: "))
substring = str(input("Enter a substring: "))

result = is_in_str(string_obj, substring)
if result:
    print(f"The string '{string_obj}' is in '{substring}'")
else:
    print(f"The string '{string_obj}' ism't in '{substring}'")

