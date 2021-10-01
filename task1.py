# -*- coding: utf-8 -*-
import csv
from datetime import datetime

input_filename = 'data.csv'
try:
    with open(input_filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        try:
            next(reader) #skip headers
        except StopIteration:
            exit()
        data_out = {}
        poses = set() 
        for row in reader:
            try:
                date = datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S')
                pos = int(row[1])
                amount = float(row[2])
            except (ValueError, IndexError):
                print('Row with invalid format.')
                print(row)
                exit()
            poses.add(pos)
            if date in data_out:
                if pos in data_out[date]:
                    data_out[date][pos] += amount
                else:
                    data_out[date][pos] = amount
            else:
                data_out[date] = {pos:amount}
except FileNotFoundError:
    print(f'File {input_filename} not found.')
    exit()

with open('data_out.csv','w') as out_file:
    out_file.write('Data/Pos;')
    n_pos = len(poses)
    i = 0
    for pos in sorted(poses):
        out_file.write(str(pos)+';')
        out_file.write(str(pos))
        if i!=n_pos-1:
            out_file.write(';')
        i+=1
    out_file.write('\n')
    for date in sorted(data_out.keys()):
        out_file.write(str(date)+';')
        i = 0
        day_data = data_out[date]
        day_sum = sum([day_data[pos] for pos in day_data])
        for pos in sorted(poses):
            try:
                out_file.write("{:.2f};".format(day_data[pos]))
                out_file.write(str(int(day_data[pos]/day_sum*100))+'%')
            except KeyError:
                out_file.write('0;')
                out_file.write('0%')
            if i!=n_pos-1:
                out_file.write(';')
            i+=1
        out_file.write('\n')
