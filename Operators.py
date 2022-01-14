# enumerate creates tuples of iterable object and its index
word = 'Shreya'

for i in enumerate(word):
    print(i)

# to unpack the tuple and just get the letters
for i, j in enumerate(word):
    print(j)

# to get index also and print format
for i, j in enumerate(word):
    print(f'Letter at index {i} is {j}')

# zip is used to combine different lists into tuple pairs
l1 = [1, 3, 2]
l2 = ['a', 'b', 'c']

for i in zip(l1, l2):
    print(i)

l3 = ['A', 'B', 'C']

for i,j in zip(l1, l3):
    print(j)

for i in zip(l1,l2,l3):
    print(i)

# to make the zip a list, typecast it

l = list(zip(l1,l2,l3))
print(l)

result = int(input('Enter a number here: '))
print(result)