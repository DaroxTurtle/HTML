print('N5.4_041023.py Test')

found = False
print('Before', found)
for value in [9 ,41, 12, 3, 74, 15] :
    if value == 3:
        found = True
    print(found, value)
    found = False
print('After', found)