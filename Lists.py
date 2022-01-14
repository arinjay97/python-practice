list_a = ["hello", 1, 2.01]

print(len(list_a))
print(list_a[2])

list_b = ["20", 5]

list_c = list_a + list_b
print(list_c)
list_c.append("appended")
list_c.append("appended after append")
print(list_c)
popped = list_c.pop(4)
print(popped)
print(list_c)

list_d = ['a', 'n', 'c']
list_d.sort()
print(list_d)

# list comprehensions is equivalent to iterating using a for. can add any operations
word = 'Hello'
l = [x for x in word]
print(l)
l1 = [x for x in range(0, 11)]
print(l1)
l2 = [x*2 for x in range(0, 10) if not x % 2 == 0]
print(l2)
l3 = [x if x % 2 == 0 else 'Odd' for x in range(0,11)]
print(l3)

# nested loop here
l4 = [x*y for x in [1, 2, 3] for y in [1, 10, 100]]
print(l4)