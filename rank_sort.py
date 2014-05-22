#! /usr/bin/python

import re
iregex = re.compile(r'(\d+)\(')

en_rank = open('en_rank.sort_m', 'r')
ranksort = en_rank.readlines()

N = 20
infile = []
for i in range(N):
	infile.append(open('en'+str(i+1), 'r'))

outfile = []
for i in range(N):
	outfile.append(open('en'+str(i+1)+'.rank', 'w'))

sentence = []
for i in range(N):
	sentence.append(infile[i].readlines())

for i in range(len(ranksort)):
	if (i%2) != 0:
		ts = iregex.findall(ranksort[i])
		ls = len(ts)
		for j in range(ls):
			print int(ts[j])-1, (i+1)/2
			temp = sentence[int(ts[j])-1][(i-1)/2]
			print >>outfile[j], temp.strip('\n')
