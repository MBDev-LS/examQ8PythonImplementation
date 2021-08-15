while True:
    max = input('Enter the max you would like: ')
    try:
        max = int(max) + 1
    except:
        print('Please enter a valid number.')
    else:
        break
for i in range(1, max):
    output = ''
    if i % 3 == 0:
        output += 'Fizz'
    if i % 5 == 0:
        output += 'Buzz'
    print(i if len(output) == 0 else output)