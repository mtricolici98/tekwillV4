string = input("Enter some text here:")
string_reversed = string[::-1]
if string == string_reversed:
    print(f"The string \"{string}\" is a palindrome.")
else:
    print(f"The string \"{string}\" is not a palindrome.")
