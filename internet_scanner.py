#!/usr/bin/python3

from hackerman.scanners import tcp
import argparse, _thread

done = False
ignore = []

def my_thread(port, out_func=print):
	while not done:
		ip = tcp.rand_ipv4()
		while ip in ignore:
			ip = tcp.rand_ipv4()
		ignore.append(ip)
		if tcp.knock(ip,port):
			out_func(ip+":"+str(port))

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-t","--threads",
		help=("Number of threads to run. Eg: --threads 20"),
		required=True,
		type=int)
	parser.add_argument(
		"-p","--port",
		help=("Port to scan for. Eg: --port 80"),
		required=True,
		type=int)
	return parser.parse_args()

def main(args):
	started = 0
	while started < args.threads:
		_thread.start_new_thread(my_thread, (args.port, ))
		started += 1
	while True:
		try:
			pass
		except KeyboardInterrupt:
			break
	return 0

if __name__ == "__main__":
	exit(main(parse_args()))
