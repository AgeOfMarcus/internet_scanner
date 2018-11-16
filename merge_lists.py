#!/usr/bin/python3

import sys

try:
	list_1 = sys.argv[1]
	list_2 = sys.argv[2]
except:
	print("Args needed, list_1, list_2")
	exit(1)

l1 = open(list_1,"r").read().split("\n")
l2 = open(list_2,"r").read().split("\n")
out = l1

for i in l2:
	if i in l1:
		continue
	else:
		out.append(i)

with open("out.txt","w") as f:
	f.write(out[0])
	for i in out[1:]:
		f.write("\n"+i)
