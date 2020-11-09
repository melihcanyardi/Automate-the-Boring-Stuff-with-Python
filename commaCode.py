def comma_code(list):
    for i in range(len(list) - 1):
        print(list[i] + ', ', end='')
    print('and ' + list[len(list) - 1])

spam = ['apples', 'bananas', 'tofu', 'cats']
comma_code(spam)