import PerWordAnalisys
import csv
reviews = []
with open('files/CleanData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            reviews.append(row[-1])
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1