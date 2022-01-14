mylist = [1, 2, 3, 4, 5, 6]
sum = 0
for i in mylist:
    if i % 2 == 0:
        print(i)
    sum = sum + i

print(sum)
print('-----------------')

t = (1, 2, 3)
l = [(1, 2), (2, 3), (3, 4)]
# unpacking tuple
for i, j in l:
    print(i)
    print(j)

print('-------------')
# generates a sequence of numbers from 0 to 11-1
range(0,11)
# change it to a list so we can print
print(list(range(0, 11)))

