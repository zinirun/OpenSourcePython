import re
import find_size
import find_value
import comp_dist
import find_index

def load_data():
    data = []
    fd = open("A.dat", 'r', encoding="utf-8")
    string_data = " ".join(fd.readlines())

    result = re.compile(r"(\d+),(\d+):(\d+)|(\d+),(\d+):(-\d+)").findall(string_data)
    for _ in result:
        temp = list(_)
        temp.remove('')
        temp.remove('')
        temp.remove('')
        temp = list(map(int, temp))
        data.append(temp)
    return data


if __name__=="__main__":
    data = load_data()

    max_row, max_col = find_size.find_size(data)
    print("------ 1 - find_size ------")
    print("max row : {} / max col : {}".format(max_row, max_col))

    max_value, min_value = find_value.find_value(data)
    
    print("------ 2 - find_value ------")
    print("max value : {} / max value : {}".format(max_value, min_value))

    print("------ 3 - comp_dist ------")
    print("euclidean_dist: {}".format(comp_dist.comp_dist(data)))

    print("------ 4 - find_index ------")
    print("* below row is less then or equal to 10.0 to the 37 row")

    for row1 in range(0, max_row):
        temp_result = find_index.find_index(data,row1,37)
        if row1 == 37:
            continue
        elif temp_result <= 10.0:
            print("- row: {} th".format(row1))
