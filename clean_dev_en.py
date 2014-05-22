#! /usr/bin/python

import os
N = 20
for i in range(N):
    command = "rm -rf dev_en" + str(i+1) + "*"
    os.system(command)
os.system('ls')
