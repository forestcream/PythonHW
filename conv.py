# id,name,birth,salary,department
# 1,Ivan,1980,150000,1
# 2,Alex,1960,200000,5
#
# 3,Ivan,,130000,8
# ->//
# output.json
#
def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def prepare_data(data):
    title = data.pop(0).strip().split(',')
    return title, data

def convert_row_to_json(keys, row):
    values = row.strip().split(',')
    dict(zip(title, values))

    print("""""{"name":{},
                "id":{},
                "birth":{},
                "salary":{},
                "department":{}
                }""".format(*values))

def convert_csv_to_json(data):
    title, data = prepare_data(data)
    result = [convert_row_to_json(title, row) for row in data]

def main():
    conv = Converter()
    conv.readInput()


if __name__ == "__main__":
    main()