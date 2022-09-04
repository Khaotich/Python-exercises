import csv

'''
csv.reader()
csv.writer()
csv.DictReader()
csv.DictWriter()
'''

with open('names.csv', 'r') as f:
    csvReader = csv.reader(f)

    with open('new_csv.csv', 'w', newline='') as f2:
        csvWriter = csv.writer(f2, delimiter='-')

        for i in csvReader:
            del i[2]
            csvWriter.writerow(i)

with open('names.csv', 'r') as f:
    csvReader = csv.DictReader(f)

    # i in csvReader:
        #del  i['email']
        #print(i)

    with open('new_names.csv', 'w') as f2:
        csv_writer = csv.DictWriter(f, fieldnames=['first_name', 'last_name'], delimiter='-')
        csv_writer.writeheader()

        for i in csvReader:
            del i['email']
            csv_writer.writerow(i)