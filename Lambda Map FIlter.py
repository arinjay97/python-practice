def sqr(num):
    return num**2

# map applies a function to every item in a list, tuple, set
l = [1, 2, 3, 4, 5]
for item in map(sqr, l):
    print(item)

# filter applies function to every item in a list, tuple, set but gives output only for a tru/false condition defined in
# the function and removes the other stuff

def even(num):
    return num%2 == 0
print(list(filter(even, l)))

# lambda expression - instead of making a function, use lambda keyword and make one time use function

print(list(map(lambda num: num**3, l)))
# this cubes every item in list l without a cube function being defined

print(list(filter(lambda num: num%2==0, l)))

# to grab first char of every word in a string
print(list(map(lambda c: c[0], ['Hello', 'World'])))

