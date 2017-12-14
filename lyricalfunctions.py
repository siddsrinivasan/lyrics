import nltk
import random
import math

###################################################################################################################
########################################## Pre Processing #########################################################
###################################################################################################################



""" Cleans up the text for a given function, allowing it to be processed"""
def cleanUp(text):
	newlist = []
	for line in text:
		for word in line:
			word = remove_brackets(word)	
		line_of_words = line.split()
		#print line_of_words
		newlist.extend(line_of_words)
	return newlist



def remove_brackets(word):
	word.replace("(","")
	word.replace(")","")
	return word


###################################################################################################################
########################################## Probability Calculations ###############################################
###################################################################################################################


## contain counts for each unigram and bigram
def unigramCounts(text):
	unigram_dict = {}
	for word in text:
		if (word not in unigram_dict):
			unigram_dict[word] = 1
		else:
			unigram_dict[word] += 1
	return unigram_dict

def bigramCounts(text):
	bigram_text = nltk.bigrams(text)
	bigram_dict = {}
	for pair in bigram_text:
		if pair not in bigram_dict:
			bigram_dict[pair] = 1
		else:
			bigram_dict[pair] += 1
	return bigram_dict


def makeSentence(text,bigram_counts, vocab_length):
	start_token = random.randint(0,len(text)-2)
	current_word = text[start_token]
	# number of lyric words is restricted to 30
	i = 60
	sentence = current_word + " "
	while (i>0):
		i = i-1
		current_word = nextWord(current_word,bigram_counts, vocab_length)
		if (current_word.find(",") >= 0 or current_word.find(".")>=0):
			next_word = current_word.replace(",",",\n")
			sentence = sentence + " " + next_word
		else:
			sentence = sentence + " " + current_word
	print sentence

def nextWord(current_word,bigram_counts, vocab_length):
	word_array = []
	next_word_score = 0
	next_word = "."
	for item in bigram_counts:
		if item[0] == current_word:
			score = bigram_counts[item]
			for x in range(0,score + 1):
				word_array.append(item[1])
	index = random.randint(0,len(word_array)-1)
	return word_array[index]












