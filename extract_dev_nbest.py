#! /usr/bin/python

import re
regex1 = re.compile(r'\|\|\| ([^|]+) \|\|\| [^|]* \|\|\|')

in_file = open('dev_nbest20', 'r')
all_lines = in_file.readlines()

N = 20
LEN = 886

out_arr = []
for i in range(N):
    out_name = 'dev_en' + str(i+1)
    out_arr.append( open(out_name, 'w') )

for j in range(LEN):
    for i in range(N):
        ts = all_lines[j*N+i]
        temp_str = regex1.findall(ts)[0]
        print >>out_arr[i], temp_str


