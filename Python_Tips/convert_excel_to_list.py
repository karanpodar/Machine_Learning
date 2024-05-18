import csv

data_list = []

with open(r'Boto3_auto\netflix_titles.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        data_list.append(row)

print(data_list[:2])