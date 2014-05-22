#! /usr/bin/python

import re
regex1 = re.compile(r'\|\|\| ([^|]+) \|\|\| [^|]* \|\|\|')
regex2 = re.compile(r'(\d+) \|\|\| [^|]+ \|\|\| [^|]+ \|\|\|')

import sys
if len(sys.argv) == 2 and sys.argv[1] == '-h':
    print "Extract lines from nbestN and output files of en(1..N)"
    print "Usage: ", sys.argv[0], "N nbest_filename"
    sys.exit()

N = int(sys.argv[1])
fname = sys.argv[2]

in_file1 = open(fname, 'r')
all_lines1 = in_file1.readlines()

#LEN = 1000

out_arr = []
for i in range(N):
    out_name = 'en' + str(i+1)
    out_arr.append( open(out_name, 'w') )


old_no = 0
file_id = 0
for i in range(len(all_lines1)):
    temp_no = regex2.findall(all_lines1[i])[0]
    ts = regex1.findall(all_lines1[i])[0]
    if int(temp_no) == old_no:
        print >>out_arr[file_id], ts
        file_id += 1
    else:
        if file_id != N:
            print temp_no, "th sentence has only", file_id, "n-best list", "line ", i+1, "file nbest01.20"
            ts_pre = regex1.findall(all_lines1[i-1])[0]
            for qq in range(file_id, N):
                print >>out_arr[qq], ts_pre
        file_id = 0
        print >>out_arr[file_id], ts
        file_id += 1
        old_no = int(temp_no)

#old_no = 0
#file_id = 0
#for i in range(len(all_lines2)):
#    temp_no = regex2.findall(all_lines2[i])[0]
#    ts = regex1.findall(all_lines2[i])[0]
#    if int(temp_no) == old_no:
#        print >>out_arr[file_id], ts
#        file_id += 1
#    else:
#        if file_id != N:
#            print temp_no, "th sentence has only", file_id, "n-best list", "line ", i+1, "file nbest02.20"
#            ts_pre = regex1.findall(all_lines2[i-1])[0]
#            for qq in range(file_id, N):
#                print >>out_arr[qq], ts_pre
#        file_id = 0
#        print >>out_arr[file_id], ts
#        file_id += 1
#        old_no = int(temp_no)

#for j in range(LEN):
#    for i in range(N):
#        ts = all_lines2[j*N+i]
#        temp_str = regex1.findall(ts)[0]
#        print >>out_arr[i], temp_str
#
#for j in range(LEN):
#    for i in range(N):
#        ts = all_lines1[j*N+i]
#        temp_str = regex1.findall(ts)[0]
#        print >>out_arr[i], temp_str




