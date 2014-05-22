#! /usr/bin/python

in_total = open("sentprob.debug", 'r')
total_lines = in_total.readlines()
in_rp = open("rankprob.debug", 'r')
rp_lines = in_rp.readlines()
in_mp = open("model1prob.debug", 'r')
mp_lines = in_mp.readlines()

of1 = open("debug.log1", 'w')
of2 = open("debug.log2", 'w')

LEN = len(total_lines)
logarr = []

for i in range(LEN):
  leftp = total_lines[i].strip('\n')
  ind = (i/19000)*1000 + (i%19000)%1000
  middlep = rp_lines[ind].strip('\n')
  rightp = mp_lines[ind].strip('\n')
  part = leftp + " ||| " + middlep + " ||| " + rightp
  logarr.append(part)
  print >>of1, part

cnt = 1000
for i in range(cnt):
    for k in range(380):
        print >>of2, logarr[k*1000+i]

