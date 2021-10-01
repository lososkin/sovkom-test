# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv
import os
import shutil

try:
    shutil.rmtree('plt')
except FileNotFoundError:
    pass
os.makedirs('plt/absolute')
os.makedirs('plt/relative')
try:
    with open('data_out.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        try:
            headers = next(reader)
        except StopIteration:
            exit()
        n = len(headers)
        data = [[] for _ in range(n)]
        for row in reader:
            for i in range(n):
                data[i].append(row[i])
        data[0] = [d[:10] for d in data[0]]
        plt.figure(figsize=(len(data[0])//5, 10), dpi=80)
        for i in range(1,n):
            if i%2:
                data[i] = [float(d) for d in data[i]]
                plt.clf()
                plt.title(f'Сумма выдач для точки {headers[i]}')
                plt.ylabel('Сумма выдач')
                plt.xlabel('Дата')
                plt.plot(data[0],data[i])
                plt.plot(data[0],data[i],'o')
                plt.xticks(rotation=90)
                plt.savefig(f'plt/absolute/{headers[i]}.png')
            else:
                data[i] = [int(d[:-1]) for d in data[i]]
                plt.clf()
                plt.title(f'Относительный объем выдач для точки {headers[i]}')
                plt.ylabel('Процент суммы выдач в точке от общей суммы')
                plt.xlabel('Дата')
                plt.plot(data[0],data[i])
                plt.plot(data[0],data[i],'o')
                plt.ylim([0,100])
                plt.xticks(rotation=90)
                plt.savefig(f'plt/relative/{headers[i]}.png')
except FileNotFoundError:
    print('File data_out.csv not found.')
