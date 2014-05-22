#! /usr/bin/python

import subprocess
import re
bleu_regex = re.compile(r'BLEU = ([^,]+),')

ofile = open('bleu-eval.output', 'w')

en = "en"
N = 20

print >>ofile, "raw", "rank"

for i in range(N):
	command1 = "./multi-bleu.perl en.ref < en" + str(i+1)
	command3 = "./multi-bleu.perl en.ref < en" + str(i+1) + ".rank"
	temp1 = subprocess.Popen([command1], stdout = subprocess.PIPE, shell = True)
	temp3 = subprocess.Popen([command3], stdout = subprocess.PIPE, shell = True)
	ans1 = bleu_regex.findall(temp1.communicate()[0])[0]
	ans3 = bleu_regex.findall(temp3.communicate()[0])[0]
	print >>ofile, ans1, ans3


print "bleu-eval process ends successfully!"

