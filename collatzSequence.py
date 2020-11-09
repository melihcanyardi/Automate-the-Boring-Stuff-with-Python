def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print('Enter number:')

try:
    number = int(input())
    while number != 1:
        number = collatz(number)
except ValueError:
    print('You must enter an integer.')