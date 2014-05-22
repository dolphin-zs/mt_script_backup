#! /usr/bin/python
#coding=utf-8

import re
regex1 = re.compile(r'\s*(\S*) \(\{')
regex2 = re.compile(r'\(\{([^\(\{\}\)]*)\}\)')

in_envcb = open('en.vcb', 'r')
in_zhvcb = open('zh.vcb', 'r')
in_ensents = open('ent_en.A3.final', 'r')
in_zhsents = open('zh', 'r')

of_ans1 = open('en_ent_zh.source', 'w')
of_ans2 = open('en_ent_zh.lsda', 'w')

LEN = 138460
print "Total length:", LEN

# reading vocabulary index files and build vocabulary map
map_envcb = {'NULL':'0'}
map_zhvcb = {'NULL':'0'}

for k in in_envcb.readlines():
  tmp = k.split()
  map_envcb[tmp[1]] = tmp[0]

for k in in_zhvcb.readlines():
  tmp = k.split()
  map_zhvcb[tmp[1]] = tmp[0]

# reading corpus files
en_lines = in_ensents.readlines()
zh_lines = in_zhsents.readlines()

for i in range(LEN):
  if (i+1)%10000 == 0:
    print "Handle", i+1, "sentences."
  zh_tmp = zh_lines[i].split()
  en_tmp = en_lines[3*i+1].split()
  en_tmp.insert(0, 'NULL')
  ans_tmp1 = ['' for q in range(len(en_tmp))]
  ans_tmp2 = ['' for q in range(len(en_tmp))]
  #print en_tmp
  ent_tmp = regex1.findall(en_lines[3*i+2])
  #print ent_tmp
  al_tmp = regex2.findall(en_lines[3*i+2])
  #print al_tmp
  len_tmp = len(al_tmp)
  if len_tmp != len(ent_tmp):
    print "ERROR!"
  for j in range(len_tmp):
    al_sl = al_tmp[j].split()
    #print al_sl,
    for k in al_sl:
      ans_tmp1[int(k)] = en_tmp[int(k)] + '/' + ent_tmp[j]
      if map_envcb.has_key(en_tmp[int(k)]) and map_envcb.has_key(ent_tmp[j]):
        ans_tmp2[int(k)] = map_envcb[en_tmp[int(k)]] + ' ' + map_envcb[ent_tmp[j]] + ' '
      else:
        print "Error with ind of", en_tmp[int(k)], ent_tmp[j], "in line ", i+1, ' ent ', j+1

  del ans_tmp1[0]
  del ans_tmp2[0]
  #output original sentence into file
  print >>of_ans1, i+1
  print >>of_ans1, ' '.join(zh_tmp)
  print >>of_ans1, ' '.join(ans_tmp1)
  #output the word id number into file
  print >>of_ans2, i+1
  for qq in zh_tmp:
    print >>of_ans2, map_zhvcb[qq],
  print >>of_ans2, ''
  print >>of_ans2, ' '.join(ans_tmp2)
  #print ans_tmp1
  #print ans_tmp2

  #print regex1.findall(en_lines[3*i+2])
  #for j in regex2.findall(en_lines[3*i+2]):
  #  print j.split(),
  #print

print "END Successfully."
#of_debug = open('zh_id', 'w')
#for k in in_zhsents.readlines():
#  tmp = k.split()
#  for i in tmp:
#    print >>of_debug, map_zhvcb[i],
#  print >>of_debug, ''








