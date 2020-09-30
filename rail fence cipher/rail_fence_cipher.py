import numpy as np

def rail_matrix(text, rows):
    arr = np.empty((rows, len(text)), dtype='U') # 'U' for unicode
    i = 0 # i for rows
    j = 0 # for columns
    #index = 0
    direction_down = True
    for x in text:
        if i == (rows-1):
            direction_down = not direction_down
        elif i == 0 and j != 0:
            direction_down = not direction_down

        arr[i][j] = x
        if direction_down:
            i += 1
        else:
            i -= 1
        j += 1
    return arr

def read_rail_matrix(arr, n, col_wise = True):
    # n = len of text
    # returns a string combined from the rail matrix
    text = []

    if col_wise:
        for i in range(len(arr)):
            for j in range(n):
                if arr[i][j] != '':
                    text.append(arr[i][j])

    else: # when we have to read zig-zap i.e during decryption
        i = 0 # i for rows
        j = 0 # for columns
        direction_down = True
        rows = len(arr)
        for _ in range(n):
            if i == (rows-1):
                direction_down = not direction_down
            elif i == 0 and j != 0:
                direction_down = not direction_down

            text.append(arr[i][j])
            if direction_down:
                i += 1
            else:
                i -= 1
            j += 1
    return ''.join(text)

def encryption(pt, rows):
    # creating a required 2d numpy array
    arr = rail_matrix(pt, rows)
    # reading matrix and combining ct
    ct = read_rail_matrix(arr, len(pt))
    #print(ct)
    return ct


def decryption(ct, rows):
    # creating a arr where the correct positions are marked
    # by dashes '_'
    index = 0 # index of text
    dash = '_'*len(ct)
    arr = rail_matrix(dash, rows)
    #print(arr)
    # now filling row wise in place of _ with letters

    for i in range(len(arr)): # rows
        for j in range(len(ct)): # columns
            if arr[i][j] == '_':
                arr[i][j] = ct[index]
                index += 1
    # now we have an arr with the
    # letters placed at correct position

    # reading matrix in zig-zag
    pt = read_rail_matrix(arr, len(ct), col_wise=False)
    return pt

def main():
    rows = int(input("Enter Key: "))
    pt = input("Enter Plain Text: ")
    print("Cipher text is: ", encryption(pt, rows))
    ct = input("Enter Cipher Text: ")
    print("Plain Text: ", decryption(ct, rows))
main()
