def reverse_string(text):
    return text[::-1]

try:
    text = input("Enter a string ")
    reverse_str = reverse_string(text)
    print(f" The reverse of the given dstring is: {reverse_str}")

except Exception as e:
    print("Error occurred: {e}")