#! /usr/bin/python

import re
regex1 = re.compile(r'\|\|\| ([^|]+) \|\|\| [^|]* \|\|\|')
regex2 = re.compile(r'(\d+) \|\|\| [^|]+ \|\|\| [^|]+ \|\|\|')
import sys

n_str = sys.argv[1]

name = "nbest" + n_str
in_file = open(name, 'r')
all_lines = in_file.readlines()

N = int(n_str)
#LEN = 1000
real_cnt = N + 1

out_arr = []
for i in range(N):
    out_name = 'en' + str(i+1)
    out_arr.append( open(out_name, 'w') )

old_no = 0
file_id = 0
for i in range(len(all_lines)):
    temp_no = regex2.findall(all_lines[i])[0]
    ts = regex1.findall(all_lines[i])[0]
    if int(temp_no) == old_no:
        print >>out_arr[file_id], ts
        file_id += 1
    else:
        file_id = 0
        print >>out_arr[file_id], ts
        file_id += 1
        old_no = int(temp_no)


#for j in range(LEN):
#    for i in range(N):
#        ts = all_lines[j*N+i]
#        temp_str = regex1.findall(ts)[0]
#        print >>out_arr[i], temp_str
#

