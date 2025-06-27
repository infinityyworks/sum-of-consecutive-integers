print('What is the longest sum of consecutive positive integers that is equal to x?')
print()
target = 'a'
while not (target.isnumeric() and target != '0'):
    target = input('Enter a positive integer to be x:  ')
target = int(target)
print()
printAll = ''
while not (printAll == 'y' or printAll == 'n'):
    printAll = input('Should all possible consecutive sums be shown (y/n)?  ')
print()
n = 1
x = target

if printAll == 'y':
    while x > 0:
        x = (target - (n**2 + n) / 2) / n
        if x.is_integer():
            sum = []
            for i in range(n):
                sum.append(str(int(x + i + 1)))
            print(' + '.join(sum),'\n')
        n += 1

    print(f'Longest sum is {len(sum)} integers long.')

else:
    final_x = 0

    while x > 0:
        x = (target - (n**2 + n) / 2) / n
        if x.is_integer():
            final_x = x
        n += 1

    sum = []
    for i in range(n):
        sum.append(str(int(final_x + i + 1)))

    print(' + '.join(sum),'\n')
    print(f'Longest sum is {len(sum)} integers long.')
