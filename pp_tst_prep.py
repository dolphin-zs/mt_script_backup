#! /usr/bin/python

en_name = ''
import sys
if len(sys.argv) == 1:
    print "Usage: " + sys.argv[0] + " en "
    sys.exit()
else:
    print "en_name = " + sys.argv[1]
    en_name = sys.argv[1]

N = 20
LEN = 1000

in_en = []
for i in range(N):
    fn = en_name + str(i+1)
    in_en.append(open(fn, 'r'))

en_sents = []
for i in range(N):
    en_sents.append(in_en[i].readlines())

of_en = open('test_en', 'w')
of_ent = open('test_ent', 'w')

for i in range(N):
    for j in range(N):
        if i != j:
            for k in range(LEN):
                print >>of_en, en_sents[i][k].strip('\n')
                print >>of_ent, en_sents[j][k].strip('\n')


