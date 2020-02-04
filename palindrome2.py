def palindrome(s):
    return s == s[::-1]
s = input('Enter a string:')
if palindrome(s):
    print("a palindrome")
else:
    print("no a palindrome")

