# find out if the word 'dog' is in a string


def dog_check(string):
    if 'dog' in string.lower():
        return 'Dog is in string'
    else:
        return 'Dog is not in string'


def pig_latin(s):
    if s[0] in 'aeiou':
        return s + 'ay'
    else:
        return s[1:] + s[0] + 'ay'


print(pig_latin('word'))
print(pig_latin('apple'))
