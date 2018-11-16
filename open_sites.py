#!/usr/bin/python3

import sys, os

try:
	num = int(sys.argv[1])
except:
	num = 10

sites = open("sites.txt","r").read().split("\n")
to_open = sites[:num]

cmd = "firefox "
cmd_a = "-new-tab -url %s "

for ip in to_open:
	if ip in open("ignore.txt","r").read().split("\n"):
		sites.remove(ip)
		continue
	url = "http://"+ip
	cmd += (cmd_a % url)
	sites.remove(ip)
with open("sites.txt","w") as f:
	f.write(sites[0])
	for i in sites[1:]:
		f.write("\n"+i)

os.system(cmd)
for i in to_open:
	os.system("echo %s >> ignore.txt" % i)

