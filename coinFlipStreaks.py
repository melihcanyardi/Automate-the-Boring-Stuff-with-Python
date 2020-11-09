import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    hundred_flips = []
    for flip in range(100):
        if random.randint(0, 1) == 0:
            hundred_flips.append('H')
        else:
            hundred_flips.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    all_flips = ''
    for i in range(len(hundred_flips) - 1):
        all_flips += hundred_flips[i]

    if 'HHHHHH' in all_flips or 'TTTTTT' in all_flips:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))