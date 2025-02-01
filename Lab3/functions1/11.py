def is_palindrome(s):
    s_cleaned = ''.join(s.split()).lower()
    return s_cleaned == s_cleaned[::-1]


print(is_palindrome("madam"))
print(is_palindrome("nurses run"))
print(is_palindrome("KBTU"))