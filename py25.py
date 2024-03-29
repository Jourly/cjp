#encoding = utf-8
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return  sorted(words)
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	print words.pop(0)
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	print words.pop(-2)
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
#sorted(排序一个List或者Iterator，默认为升序)
#split('')以某字符切割字符串
#pop（n）删除第n+1个值


	
