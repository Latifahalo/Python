s = 0
name = input("What is your name? ")
print('Hello', name)

color = input("What is your favorite color? ")
if color == 'red':
    s += 1
elif color == 'green':
    s -= 1
elif color == 'blue':
    s -= 2

food = input('What is your favorite food? ')
if food == 'pasta':
    s += 1
elif food == 'eggs':
    s -= 1

if s <= 1:
    print('GOOD')
else:
    print('NICE')


