# Основная программа
from loadpairs import loadpairs
from get_q_templs import get_q_templs
from gram_filter import gram_filter
from ngram import train
from json import dumps
from pymystem3 import Mystem
from generate_sentence import generate_sentence

ma = Mystem()

pairs = loadpairs(filename = 'data.json') 
q_templs = get_q_templs( 
	znanie = pairs, 
	kolvo = 5, 
	form = "Правда ли что %s %s %s?")
model = train(corpus = 'voprosi')
questions = gram_filter(q_templs,model) 
#print(questions)
kutokens = []
for question in questions:
	kutokens = []
	for a in ma.analyze(question):
		try:
			_ = a['analysis'][0]['lex']
			kutokens += [_]
		except (KeyError, IndexError):
			pass
	#print(kutokens)
	print(generate_sentence(model,kutokens))
