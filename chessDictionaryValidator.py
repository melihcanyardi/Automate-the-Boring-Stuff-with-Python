# KEYS:
# 1a 1b 1c ... 1h
# 2a 2b 2c ... 2h
# ...
# 8a 8b 8c ... 8h

# VALUES:
# bpawn bknight bbishop brook bqueen bking
# wpawn wknight wbishop wrook wqueen wking

# Rules:
# One black king & one white king,
# 16 pieces at most for each player,
# 8 pawns at most for each player,


def isValidChessBoard(dict):
    valid = True

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    for k in dict.keys():
        if k[0] not in numbers or k[1] not in letters:
            valid = False

    chessPieces = []
    for v in dict.values():
        chessPieces.append(v)
    if ('bking' not in chessPieces) or ('wking' not in chessPieces):
        valid = False
    if chessPieces.count('bking') > 1 or chessPieces.count('wking') > 1:
        valid = False

    count = 0
    for piece in chessPieces:
        count += 1
    if count > 16:
        return False

    if (chessPieces.count('bpawn') > 8) or (chessPieces.count('wpawn') > 8):
        valid = False

    return valid

# Testing boards (from r/learnpython
print(isValidChessBoard({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))  # True
print(isValidChessBoard({"1a": "bpawn", "2a": "wking"}))  # False: no bking
print(isValidChessBoard({"1a": "wking", "2a": "wking", "3c": "bbishop"}))  # False: cannot have 2 white kings, no bking
print(isValidChessBoard({"1a": "bking", "9z": "wking"}))  # False: 9z is an invalid position
