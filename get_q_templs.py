# Генерация вопросов

from random import randint

def get_q_templs( 
		znanie = {}, 
		kolvo = 5, 
		form = "Правда ли что %s %s %s?"):
	rez = {}
	i = 1
	for d1, rel, d2 in znanie.keys():
		if i > kolvo: break
		if randint(0,10) > 2:
			if randint(0,1):
				rez.update({
					form % (d2, rel, d1):{
						"a":{"text":"да", "correct": 1}, 
						"b":{"text":"нет", "correct": 0}, 
						"c":{"text":"не знаю", "correct": 0}, 
					}
				})
			else:
				for _d1, _rel, _d2 in znanie.keys():
					if _d1 != d1 and rel != _rel:
						rez.update({
							form % (_d2, rel, d1):{
								"a":{"text":"да", "correct": 0}, 
								"b":{"text":"нет", "correct": 1}, 
								"c":{"text":"не знаю", "correct": 0}, 
							}
						})
						break
			i += 1
	return rez
	
if __name__ == '__main__':
	print(get_q_templs( # list of str
		znanie = {('брикетирование', 'мочь быть', 'прессование'): 1, ('брикетирование', 'помогать', 'разделение мусор'): 1, ('разделение мусор', 'производить', 'вторичный сырье'): 1, ('захоронение', 'являться', 'свалка'): 1, ('свалка', 'иметь', 'влияние'): 1}, 
		kolvo = 1, 
		form = "%s) Правда ли что %s %s %s?"))
