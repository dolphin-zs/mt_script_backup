#! /usr/bin/python

yita = 1.0

import sys
if len(sys.argv) == 1:
    print "Usage: " + sys.argv[0] + " yita "
    sys.exit()
elif len(sys.argv) == 2:
    yita = float(sys.argv[1])
else:
    print "Arguments Error!"
    print "Usage: " + sys.argv[0] + " yita "
    sys.exit()


import subprocess
import re
regex1 = re.compile(r'\|\|\| ([^|]+) \|\|\| [^|]* \|\|\|')
regex2 = re.compile(r'\|\|\| ([^|]+)\n')
regex3 = re.compile(r'(\d+)\( ')
regex4 = re.compile(r'\( ([^()]+) \)')
bleu_regex = re.compile(r'BLEU = ([^,]+),')

class fs_logp:
    def __init__(self, i, q):
        self.nof = i
        self.logp = q

def key_nof(test):
    return test.nof

def key_logp(test):
    return test.logp

in_file1 = open('en_nbest20', 'r')
all_lines1 = in_file1.readlines()
in_file2 = open('en_rank.sort', 'r')
all_lines2 = in_file2.readlines()


N = 20
LEN = 1000

#in_en = []
#for i in range(N):
#    name = 'dev_en' + str(i+1)
#    in_en.append( open(name, 'r') )
#
#en_sents = []
#for i in range(N):
#    en_sents.append( in_en[i].readlines() )


raw_array = []
rank_array = []
for j in range(LEN):
    raw_array.append([])
    rank_array.append([])


for j in range(LEN):
    for i in range(N):
        ts = all_lines1[j*N+i]
        tlogp = regex2.findall(ts)[0]
        raw_array[j].append( fs_logp( i+1, float(tlogp) ) )
    ts = all_lines2[2*j+1]
    arr_no = regex3.findall(ts)
    arr_logp = regex4.findall(ts)
    if len(arr_no) != len(arr_logp):
        print "ERROR IN REGEX3 4", "line", j
    for k in range(len(arr_no)):
        rank_array[j].append( fs_logp( int(arr_no[k]), float(arr_logp[k])/50 ) )
    rank_array[j].sort(key = key_nof) # sort by nof


of_name = 'output.yita-' + str(yita)
ans = open(of_name, 'w')

print >>ans, "************   yita*raw_score + (1-yita)*rank_score   ***************** "
print >>ans, ""

print >>ans, "raw      ",
for i in range(N):
    command = "./multi-bleu.perl en.ref < en" + str(i+1)
    temp = subprocess.Popen( [command], stdout = subprocess.PIPE, shell = True)
    resl = bleu_regex.findall(temp.communicate()[0])[0]
    print >>ans, resl,
print >>ans, ''


out_file = []
tuning_array = []
for j in range(LEN):
    tuning_array.append([])
for i in range(N):
    name = "en" + str(i+1) + ".yita=" + str(yita)
    out_file.append( open(name, 'w') )

for j in range(LEN):
    if len(raw_array[j]) != len(rank_array[j]):
        print "ERROR IN length. line", j
    t1 = raw_array[j]
    t2 = rank_array[j]
    for i in range(len(rank_array[j])):
        if t1[i].nof != t2[i].nof:
            print "ERROR IN SORT. line", j, "NUMBER", i
        tuning_array[j].append( fs_logp( t1[i].nof, yita*t1[i].logp + (1-yita)*t2[i].logp) )

    tuning_array[j].sort(key = key_logp, reverse = True)
    for i in range(len(tuning_array[j])):
        #print >>out_file[i], en_sents[ tuning_array[j][i].nof-1 ][j].strip('\n')
        print >>out_file[i], regex1.findall(all_lines1[j*N+tuning_array[j][i].nof-1])[0]

for i in range(N):
    out_file[i].close()

print >>ans, "generate ",
for i in range(N):
    command = "./multi-bleu.perl en.ref < en" + str(i+1) + ".tuning"
    temp = subprocess.Popen( [command], stdout = subprocess.PIPE, shell = True)
    resl = bleu_regex.findall(temp.communicate()[0])[0]
    print >>ans, resl,
print >>ans, "yita =", yita

ans.close()

print "Dumping to file----------->>" + of_name
import os
os.system('cat ./' + of_name)





