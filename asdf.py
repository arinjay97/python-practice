import string


def palindrome(s):
    s1 = ''.join(reversed(s))
    print(s == s1)


palindrome('helleh')

s = set(string.ascii_lowercase())
print(s)