#! /usr/bin/python
#coding=utf-8

in_pht = open('phrase-table', 'r')
pht_lines = in_pht.readlines()

in_lex_e2f = open('lex.1.e2f', 'r')
e2f_lines = in_lex_e2f.readlines()

in_lex_f2e = open('lex.1.f2e', 'r')
f2e_lines = in_lex_f2e.readlines()

of = open('phrase-table.il', 'w')
#print len(pht_lines), len(e2f_lines), len(f2e_lines)
mp_fe = {}
mp_ef = {}
for fe_pair in e2f_lines:
    fe_l = fe_pair.split()
    mp_fe[ fe_l[0]+' '+fe_l[1] ] = float(fe_l[2])
for ef_pair in f2e_lines:
    ef_l = ef_pair.split()
    mp_ef[ ef_l[0]+' '+ef_l[1] ] = float(ef_l[2])

#t1 = 'NULL Bedouin'
#print t1, mp_fe[t1]
#t2 = 'really 歌颂'
#print t2, mp_ef[t2]

score_lfe = 1.0
score_lef = 1.0
line_cnt = 0
for pht_line in pht_lines:
    line_cnt += 1
    score_lfe = 1.0
    score_lef = 1.0
    pht_list = pht_line.split('|||')
    #print pht_list
    fph = pht_list[0].split()
    eph = pht_list[1].split()
    mi_fe = {}
    mi_ef = {}
    al = pht_list[3].split()
    for sa in al:
        id_s = 0
        id_m = sa.find('-')
        id_e = len(sa)
        ali = int( sa[id_s:id_m] )
        alj = int( sa[id_m+1:id_e] )
        if mi_fe.has_key(ali):
            mi_fe[ali].append(alj)
        else:
            mi_fe[ali] = []
            mi_fe[ali].append(alj)
        if mi_ef.has_key(alj):
            mi_ef[alj].append(ali)
        else:
            mi_ef[alj] = []
            mi_ef[alj].append(ali)
    for i in range(len(fph)):
        if mi_fe.has_key(i):
            tmp_s = 0.0
            for kk in mi_fe[i]:
                tmp_s += mp_fe[ fph[i]+' '+eph[kk] ]
            tmp_s /= len(mi_fe[i])
            score_lfe *= tmp_s
        else:
            score_lfe *= mp_fe[ fph[i]+' NULL']
    for i in range(len(eph)):
        if mi_ef.has_key(i):
            tmp_s = 0.0
            for kk in mi_ef[i]:
                tmp_s += mp_ef[ eph[i]+' '+fph[kk] ]
            tmp_s /= len(mi_ef[i])
            score_lef *= tmp_s
        else:
            score_lef *= mp_ef[ eph[i]+' NULL' ]
    #print fph, eph, mi_fe, mi_ef
    #print round(score_lfe, 8), round(score_lef, 8)
    for i in range(len(pht_list)-1):
        if i != 2:
            print >>of, pht_list[i] + '|||',
        else:
            tmpsl = pht_list[2].split()
            if abs(float(tmpsl[1])-score_lfe) > 0.0001:
                print line_cnt, tmpsl[1], "score_lfe", score_lfe
            if abs(float(tmpsl[3])-score_lef) > 0.0001:
                print line_cnt, tmpsl[3], "score_lef", score_lef
            print >>of, tmpsl[0], tmpsl[1], '(', score_lfe, ')',
            print >>of, tmpsl[2], tmpsl[3], '(', score_lef, ') |||',
    print >>of, ''
    #break

