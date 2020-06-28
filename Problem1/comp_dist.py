import math

def comp_dist(data):
    row_10 = []
    row_27 = []
    dist = 0
    for element in data:
        if element[0] == 10:
            row_10.append(element)
        if element[0] == 27:
            row_27.append(element)
    row_10.sort()
    row_27.sort()
    for a,b in zip(row_10,row_27):
        dist += (a[2]-b[2])**2

    result = math.sqrt(dist)
    return result