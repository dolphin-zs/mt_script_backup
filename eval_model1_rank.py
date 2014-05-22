#! /usr/bin/python

import subprocess
import re
iregex = re.compile(r'(\d+)\(')
bleu_regex = re.compile(r'BLEU = ([^,]+),')

en_rank = open('en_rank.sort', 'r')
rank_lines = en_rank.readlines()
en_model1 = open("en_model1.sort", 'r')
model1_lines = en_model1.readlines()

N = 20
infile = []
for i in range(N):
    infile.append(open('en'+str(i+1), 'r'))

sentences = []
for i in range(N):
    sentences.append(infile[i].readlines())


outfile1 = []
outfile2 = []
for i in range(N):
    outfile1.append(open('en'+str(i+1)+'.rank', 'w'))
    outfile2.append(open('en'+str(i+1)+'.model1', 'w'))

LEN = 1000*2
for i in range(LEN):
    if (i%2) != 0:
        ts1 = iregex.findall(rank_lines[i])
        ts2 = iregex.findall(model1_lines[i])
        ls = len(ts1)
        for j in range(ls):
            print int(ts1[j])-1, (i+1)/2
            temp1 = sentences[int(ts1[j])-1][(i-1)/2]
            print >>outfile1[j], temp1.strip('\n')
            temp2 = sentences[int(ts2[j])-1][(i-1)/2]
            print >>outfile2[j], temp2.strip('\n')


ans = open('bleu_evaluation.output', 'w')
print >>ans, "raw   ",
for i in range(N):
    command = "./multi-bleu.perl en.ref < en" + str(i+1)
    temp = subprocess.Popen( [command], stdout = subprocess.PIPE, shell = True)
    resl = bleu_regex.findall(temp.communicate()[0])[0]
    print >>ans, resl,
print >>ans, ''

print >>ans, "model1",
for i in range(N):
    command = "./multi-bleu.perl en.ref < en" + str(i+1) + '.model1'
    temp = subprocess.Popen( [command], stdout = subprocess.PIPE, shell = True)
    resl = bleu_regex.findall(temp.communicate()[0])[0]
    print >>ans, resl,
print >>ans, ''

print >>ans, "rank  ",
for i in range(N):
    command = "./multi-bleu.perl en.ref < en" + str(i+1) + '.rank'
    temp = subprocess.Popen( [command], stdout = subprocess.PIPE, shell = True)
    resl = bleu_regex.findall(temp.communicate()[0])[0]
    print >>ans, resl,
print >>ans, ''


