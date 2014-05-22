#! /usr/bin/python

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

ans = open('output.multi', 'w')

n_arr = [2,4,6,8,10,12,14,16,18,20]
No_all = 20
N = 2
LEN = 1000

print "START multieval.py"

in_en = []
for i in range(No_all):
    name = 'en' + str(i+1)
    in_en.append( open(name, 'r') )

en_sents = []
for i in range(No_all):
    en_sents.append( in_en[i].readlines() )

for N in n_arr:
    print "......................N =", N,"........................"

    print >>ans, "N =", N
    print >>ans, "raw  ",
    for i in range(N):
        command = "./multi-bleu.perl en.ref < en" + str(i+1)
        temp = subprocess.Popen( [command], stdout = subprocess.PIPE, shell = True)
        resl = bleu_regex.findall(temp.communicate()[0])[0]
        print >>ans, resl,
    print >>ans, ''

    rs_name = "en_rank.sort" + str(N)
    in_file = open(rs_name, 'r')
    all_lines = in_file.readlines()
    print "read rank_sort information from", rs_name

    if len(all_lines) != 2*LEN:
        print "ERROR in corpus length", "N", N

    print "output sorted en file to",
    out_file = []
    for i in range(N):
        name = "en" + str(i+1) +".rank" + str(N)
        print name,
        out_file.append( open(name, 'w') )
    print ""

    for j in range(LEN):
        ts = all_lines[2*j+1]
        arr_no = regex3.findall(ts)
        if len(arr_no) != N:
            print "ERROR IN REGEX3", "line", j, "N", N
        for k in range(N):
            print >>out_file[k], en_sents[ int(arr_no[k])-1 ][j].strip('\n')

    for i in range(N):
        out_file[i].close()

    print >>ans, "rank ",
    for i in range(N):
        command = "./multi-bleu.perl en.ref < en" + str(i+1) + ".rank" + str(N)
        print "$$$execute command:", command
        temp = subprocess.Popen( [command], stdout = subprocess.PIPE, shell = True)
        resl = bleu_regex.findall(temp.communicate()[0])[0]
        print >>ans, resl,
    print >>ans, ''

    in_file.close()






