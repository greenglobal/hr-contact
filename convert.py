#!usr/bin/env python3

import pandas as pd


GOOGLE_CSV_FILE = './google-csv-headers.txt'
DATA_SOURCE_FILE = './hr-data.csv'
OUTPUT_FILE = './output.csv'


def normalizeDate(sdate):
    arr = sdate.split('/')
    return '-'.join([arr[2], arr[0], arr[1]])


def extract(row):
    return dict(
        name=row[4],
        birthday=row[6],
        email=row[8],
        address=row[10],
        phone=row[11]
    )


def write_contact(content):
    with open(OUTPUT_FILE, 'w') as fs:
        fs.write(content)


def create_row(entry, headers):
    fields = []
    for x in headers:
        fields.append('')

    fields[0] = entry['name']
    fields[14] = normalizeDate(str(entry['birthday']))
    fields[30] = str(entry['email'])
    fields[45] = str(entry['address'])
    phones = str(entry['phone']).split('\r\n')
    if len(phones) > 0:
        fields[39] = phones[0]
    if len(phones) > 1:
        fields[41] = phones[1]
    print(fields)
    return ','.join(fields)


def build(entries, headers):
    lines = [','.join(headers)]
    for entry in entries:
        row = create_row(entry, headers)
        lines.append(row)
    return '\n'.join(lines)


def init():
    headers = []
    with open(GOOGLE_CSV_FILE, 'r') as fs:
        column_names = fs.read().strip().split(',')
        for col in column_names:
            headers.append(col)

    print('/google csv headers')
    i = 0
    for k in headers:
        print(i, k)
        i += 1

    d = pd.read_csv(DATA_SOURCE_FILE)
    entries = [extract(item) for item in d.values]
    content = build(entries, headers)
    write_contact(content)


if __name__ == '__main__':
    init()
