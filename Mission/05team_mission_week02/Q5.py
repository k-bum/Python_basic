content = []
sum_list = []

class ReadCSV() :
    def __init__(self, file_path) :
        self.file_path = file_path

    def read_file(self) :
        f = open(file_path, "r", encoding = "utf8")
        while 1 :
            data = f.readline().rstrip('\n')
            if not data :
                break
            else :
                content.append(data.split(","))
        return content

    def merge_list(self) :
        content = []
        sum_list = []
        sum = 0
        
        f = open(file_path, "r", encoding = "utf8")
        while 1 :
            data = f.readline().rstrip('\n')
            if not data :
                break
            else :
                content.append(data.split(','))
        for i in range(len(content)) :
                for j in range(len(content[i])) :
                    sum = sum + int(content[i][j])
                sum_list.append(sum / 4)
                sum = 0
        sum_list.sort()
        return sum_list

file_path = "data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.merge_list())