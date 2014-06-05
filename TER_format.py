#! /usr/bin/python


import sys
if len(sys.argv) != 3:
    print "Usage:", sys.argv[0], "hyp ref"
    sys.exit(1)
hyp_fn = sys.argv[1]
ref_fn = sys.argv[2]

of_hyp = open('test.TER.hyp', 'w')
of_ref = open('test.TER.ref', 'w')

in_hyp = open(hyp_fn, 'r')
in_ref = open(ref_fn, 'r')
hyp_lines = in_hyp.readlines()
ref_lines = in_ref.readlines()
if len(hyp_lines) != len(ref_lines):
    print "LENGTH ERROR:", hyp_fn, ref_fn
    sys.exit(1)
LEN = len(hyp_lines)

for i in range(LEN):
    print >>of_hyp, hyp_lines[i].strip('\n'), "(", i+1, ")"
    print >>of_ref, ref_lines[i].strip('\n'), "(", i+1, ")"

