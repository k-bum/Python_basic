content = []
from pprint import pprint

def read_file(file_path) :
    f = open(file_path, "r", encoding = "utf8")
    while 1 :
        data = f.readline().rstrip('\n')
        if not data :
            break
        else :
            content.append(data.split(','))
    return content

file_path = "data-01-test-score.csv"
pprint(read_file(file_path))