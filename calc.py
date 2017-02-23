#coding=UTF-8

import argparse
import re
import operator

def main(file):
	content = ''
	with open(file, 'r') as f:
		content = f.read()
	words = re.split(' |\n', content)
	p = {}
	w1 = 0
	for w_utf8 in words:
		w2 = w_utf8.decode("utf-8")
		if (len(w2)) < 2:
			w1 = 0
			continue;
			
		if w1 == 0:
			w1 = w2
			continue

		w = w1 + w2
		w1 = w2
		
		if w in p:
			p[w] = p[w] + 1
		else:
			p[w] = 1

	p2 = sorted(p.items(), key=operator.itemgetter(1), reverse=True)
	for p in p2[:10]:
		print p[0] + ":" + str(p[1])

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='the file name that you want to calculate')
	args = parser.parse_args()
	main(args.file)
