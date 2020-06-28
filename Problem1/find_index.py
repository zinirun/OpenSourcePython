import math

def find_index(data, row1, row2):
    dist = 0
    row_1 = []
    row_2 = []
    for _ in data:
        if _[0] == row1:
            row_1.append(_)
        if _[0] == row2:
            row_2.append(_)

    row_1.sort()
    row_2.sort()

    for a,b in zip(row_1, row_2):
        dist += (a[2]-b[2])**2

    return math.sqrt(dist)