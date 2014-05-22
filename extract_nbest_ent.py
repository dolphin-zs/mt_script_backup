#! /usr/bin/python

import re
regex1 = re.compile(r'\|\|\| ([^|]+) \|\|\| [^|]* \|\|\|')
regex2 = re.compile(r'(\d+) \|\|\| [^|]+ \|\|\| [^|]+ \|\|\|')
import sys
if len(sys.argv) == 2 and sys.argv[1] == '-h':
    print "Extract lines from nbest01.20 and nbest02.20 and output files of en_tran(1..N)"
    sys.exit()

in_file1 = open('nbest01.20', 'r')
all_lines1 = in_file1.readlines()
in_file2 = open('nbest02.20', 'r')
all_lines2 = in_file2.readlines()

N = 20
LEN = 69230
#LEN = 1000

out_arr = []
for i in range(N):
    out_name = 'en_tran' + str(i+1)
    out_arr.append( open(out_name, 'w') )

for j in range(LEN):
    for i in range(N):
        ts = all_lines2[j*N+i]
        temp_str = regex1.findall(ts)[0]
        print >>out_arr[i], temp_str

for j in range(LEN):
    for i in range(N):
        ts = all_lines1[j*N+i]
        temp_str = regex1.findall(ts)[0]
        print >>out_arr[i], temp_str


#old_no = 0
#file_id = 0
#for i in range(len(all_lines1)):
#    temp_no = regex2.findall(all_lines1[i])[0]
#    ts = regex1.findall(all_lines1[i])[0]
#    if int(temp_no) == old_no:
#        print >>out_arr[file_id], ts
#        file_id += 1
#    else:
#        file_id = 0
#        print >>out_arr[file_id], ts
#        file_id += 1
#        old_no = int(temp_no)




