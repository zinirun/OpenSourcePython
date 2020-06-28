def find_size(data):
    max_row = sorted(data, key = lambda x: x[0], reverse=True)
    max_col = sorted(data, key = lambda x: x[1], reverse=True)
    return max_row[0][0]+1, max_col[0][1]+1