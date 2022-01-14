d1 = {'k1': 1, 'k2': 2}
print(d1['k1'])

d2 = {'k1': 1, 'k2': [0,1,2], 'k3': {'innerK': 69}}
print(d2['k1'])
print(d2['k2'][2])
print(d2['k3']['innerK'])

d = {'k1': ['a', 'b', 'c']}
print(d['k1'][2].upper())
d['k1'].append('d')
print(d)
