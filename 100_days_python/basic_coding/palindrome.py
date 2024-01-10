def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

try:
    text = input(" Enter a text ")
    
    if palindrome(text):
        print(f"The given text {text} is a palindrome")
    else:
        print(f"The given text {text} is not a palindrome")
except ValueError:
    print("Enter a valid text ")