#coding=UTF-8

import argparse
import re
import operator

def main(file):
	content = ''
	skipped_chars = ['', '\xef\xbc\x8c', '\xe3\x80\x82', '\xef\xbc\x9b', 
		'\xe3\x80\x81', '\xe2\x80\x95', '\xef\xbc\x9a', '\xe2\x80\x9c', '\xe2\x80\x9d']
	with open(file, 'r') as f:
		content = f.read()
	words = re.split(' |\n', content)
	p = {}
	for w in words:
		if w in skipped_chars:
			continue
			
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
