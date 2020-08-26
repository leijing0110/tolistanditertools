# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import itertools

import sys
import os


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


path = os.path.abspath(os.path.dirname('__file__'))
type = sys.getfilesystemencoding()
sys.stdout = Logger('log0325.txt')

print(path)
print(os.path.dirname('__file__'))
print('------------------')

filename = 'C:\\题面\\test20200325.csv'
f = open(filename, 'r', errors='ignore', encoding='UTF8')
dfsite = pd.read_csv(f, header=None)
f.close()

dfsite.columns = ['siteid', 'elecnumber', 'price', 'month']

print(dfsite)
print(50 * '-')

train_data = np.array(dfsite)  # np.ndarray()
train_x_list = train_data.tolist()  # list
print(50 * '-')
print(train_x_list)
print(50 * '-')
# print(type(train_x_list))
# print(50*'-')

first_letter = lambda x: x[0]
# names = [['Alan',100,60,1],['Alan',200,120,2],['Adam',300,180,3], ['Wes',300,180,3]]
# for letter, names in itertools.groupby(names, first_letter):
#    print(letter, list(names)) # names is a generator

for letter, train_x_list in itertools.groupby(train_x_list, first_letter):
    print(letter, list(train_x_list))  # names is a generator