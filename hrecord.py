#! /usr/bin/env python
# coding=utf-8
f = open('hrecord.txt', 'w')
rec = '%s\t%s\t%s\t%s\t%s\t%s\n' % (
    'timestamp', 'r', 'w', 'totaltime', 'avaragetime', 'corr_ratio')
f.write(rec)
f1 = open('record.txt', 'r')
rec = f1.readlines()
for line in rec:
    f.write(line)
f1.close()
f.close()
print "BYE!"
