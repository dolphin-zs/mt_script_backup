#! /usr/bin/python

import subprocess

en = ["153  153  ", "26  26  ", "2  2  ", "156  156  "]
zh = ["0  ", "2380  ", "39  ", "2  ", "222  ", "2285  ", "21154  "]

for i in en:
    for j in zh:
        command = "cat t_ffe.prob | grep \"^" + i + j + "\""
        print command
        tt = subprocess.Popen([command], stdout = subprocess.PIPE, shell = True)
        ans = tt.communicate()[0]
        print ans



