import csv
import sys

def read_csv(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        index = 0
        for row in reader:
            if index == 0:
                index += 1
                continue
            yield row

def write_csv(filename, rows):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def map_row(file_name):
    rows = []
    for row in read_csv(file_name):
        rows.append({'site': '00857A', 'apt': int(row[0]), 'util': 'E', 'charge': row[7], 'date': '20151207',
                     'total_kwh': row[4], 'start': row[3], 'end': row[2]})
    rows.sort(key=lambda x: x['apt'])

    def adjust(s, num):
        return s.rjust(num, '0')

    csv_comma_rows = []
    csv_rows = []


    for row in rows:
        r = [row['site'], adjust(str(row['apt']), 6), row['util'], adjust(row['charge'], 9), row['date'],
             adjust(row['total_kwh'], 9),
             adjust(row['start'], 9),adjust(row['end'], 9)]
        csv_comma_rows.append(r)
        csv_rows.append([''.join(r)])

    comma_file = '%s_comma.txt' % file_name
    print 'writing comma delimited file - %s' % comma_file
    write_csv(comma_file, csv_comma_rows)

    no_comma_file = '%s_no_comma.txt' % file_name
    print 'writing no comma delimited file  - %s' % no_comma_file
    write_csv(no_comma_file, csv_rows)






if __name__ == '__main__':
    print sys.argv[2]
    #url = 'mtr_nov.csv'
    map_row(sys.argv[2])
    print 'done'