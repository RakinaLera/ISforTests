# Получение N-грамм

import re
from collections import defaultdict
from random import uniform

r_alphabet = re.compile(u'[а-яА-Я0-9-]+|[.,:;?!]+')
r_jo = re.compile('ё')

def train(corpus = 'voprosi'):
	lines = gen_lines(corpus)
	tokens = gen_tokens(lines)
	trigrams = gen_trigrams(tokens)

	bi, tri = defaultdict(lambda: 0.0), defaultdict(lambda: 0.0)

	for t0, t1, t2 in trigrams:
		bi[t0, t1] += 1
		tri[t0, t1, t2] += 1

	model = {}
	for (t0, t1, t2), freq in tri.items():
		if (t0, t1) in model:
			model[t0, t1].append((t2, freq/bi[t0, t1]))
		else:
			model[t0, t1] = [(t2, freq/bi[t0, t1])]
	return model

def gen_lines(corpus):
	data = open(corpus)
	for line in data:
		yield re.sub(r_jo, 'е', line.lower())

def gen_tokens(lines):
	for line in lines:
		for token in r_alphabet.findall(line):
			yield token

def gen_trigrams(tokens):
	t0, t1 = '$', '$'
	for t2 in tokens:
		yield t0, t1, t2
		if t2 in '.!?':
			yield t1, t2, '$'
			yield t2, '$','$'
			t0, t1 = '$', '$'
		else:
			t0, t1 = t1, t2

if __name__ == '__main__': 
	print(train('voprosi'))
