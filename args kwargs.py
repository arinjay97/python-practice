# *args used when number of parameters in a function aren't known as a tuple
def f(*args):
    return sum(args)


# **kwargs used when number of parameters not known but returns a dictionary with key value pairs
def g(**kwargs):
        if 'fruit' in kwargs:
            print('My favorite fruit is {}'.format(kwargs['fruit']))
        if 'veggies' in kwargs:
            print('My favorite veggies are {}'.format(kwargs['veggies']))
        else:
            print('I did not find any food here')


g(veggies='tomato', fruit='pineapple')


def skyline(s):
    result = ''
    for i in range(1, len(s)):
        if i % 2 == 0:
            result = result + s[i].lower()
        else:
            result = result + s[i].upper()
    return s[0].lower() + result

