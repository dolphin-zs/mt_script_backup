#! /usr/bin/python

in_pht = open('phrase-table.add', 'r')
of1 = open('phrase-table.p1N', 'w')
of2 = open('phrase-table.normalize', 'w')

hstr = ''
hstr_cur = '$$$@_@$$$'
pht_map = {}
cnt_total = 0
while True:
    cnt_total += 1
    pht_line = in_pht.readline()
    pht_list = pht_line.split(' |||')
    hstr = pht_list[0]
    #print pht_list
    if hstr_cur == '$$$@_@$$$':
        hstr_cur = hstr
    if hstr_cur == hstr and pht_line != '':
        #initialize pht_map
        if pht_map.has_key(hstr_cur):
            pht_map[hstr_cur].append(pht_line)
        else:
            pht_map[hstr_cur] = []
            pht_map[hstr_cur].append(pht_line)
    else:
        NT = len(pht_map[hstr_cur])
        norm_para = 0.0
        for tmp_line in pht_map[hstr_cur]:
            tmp_list = tmp_line.split('|||')
            print >>of1, tmp_list[0]+'|||'+tmp_list[1]+'|||',
            score_list = tmp_list[2].split()
            print >>of1, score_list[0], score_list[1], score_list[2], score_list[3], score_list[4],
            print >>of1, 1.0/NT,
            print >>of1, '|||'+tmp_list[3]+'|||'+tmp_list[4]+'|||'
            norm_para += float(score_list[4])
        for tmp_line in pht_map[hstr_cur]:
            tmp_list = tmp_line.split('|||')
            print >>of2, tmp_list[0]+'|||'+tmp_list[1]+'|||',
            score_list = tmp_list[2].split()
            if NT == 1:
                print >>of2, score_list[0], score_list[1], score_list[2], score_list[3], score_list[4],
            else:
                print >>of2, score_list[0], score_list[1], score_list[2], score_list[3], float(score_list[4])/norm_para,
            print >>of2, '|||'+tmp_list[3]+'|||'+tmp_list[4]+'|||'

        pht_map.clear()
        if pht_line != '':
            hstr_cur = hstr
            pht_map[hstr] = []
            pht_map[hstr].append(pht_line)
        #if cnt_total == 20:
        #    break

    if pht_line == '':
        break


