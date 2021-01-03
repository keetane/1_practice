number = input("what's your odd number?")
number = float(number)

if number % 2 == 1:
    print('it makes sense.')
elif number % 2 == 0:
    print('chech your answer')
else:
    print('go away')