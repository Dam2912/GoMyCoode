def is_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True
    else:
        return False

# Test the function
input_string = input("Input: ")
if is_palindrome(input_string):
    print("palindrome.")
else:
    print("Not a palindrome.")
