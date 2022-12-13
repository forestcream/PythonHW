# id,name,birth,salary,department
# 1,Ivan,1980,150000,1
# 2,Alex,1960,200000,5
#
# 3,Ivan,,130000,8
# ->//
# output.json
#
import csv
import json


def make_json(csvFilePath, jsonFilePath):
    data = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)


        for row in csvReader:

            data.append(row)


    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)



csvFilePath = r'input.csv'
jsonFilePath = r'output.json'


make_json(csvFilePath, jsonFilePath)