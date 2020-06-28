def find_value(data):
    max_value = sorted(data, key = lambda x : x[2], reverse = True)
    min_value = max_value[-1][2]
    return max_value[0][2], min_value