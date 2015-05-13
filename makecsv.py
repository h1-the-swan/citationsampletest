# coding: utf-8
f = open('cit-HepTh.txt', 'r')
lines = [line.split() for line in f.readlines()]
del lines[:4]
f.close()
outf = open('cit-HepTh.csv', 'w')
for line in lines:
    outf.write(line[0] + ',' + line[1] + '\n')
outf.close()
