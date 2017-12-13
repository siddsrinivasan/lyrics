import nltk
import random



""" Cleans up the text for a given function, allowing it to be processed"""
def cleanUp(text):
	newlist = [""]
	for line in text:
		for word in line:
			word = remove_brackets(word)	
		line_of_words = line.split()
		newlist.extend(line_of_words)
	#print newlist



def remove_brackets(word):
	word = word.replace("(","")
	word = word.replace(")","")
	return word



###################################################################################################################
########################################## Probability Calculations ###############################################
###################################################################################################################


## contain counts for each unigram and bigram
def unigramCounts(text):
	unigram_dict = {}
	for word in text:
		if word not in unigram_dict:
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


def makeSentence(text,unigram_counts,bigram_counts):
	start_token = random.randint(0,len(text)-2)
	current_word = text[start_token]
	print current_word
	# number of lyric words is restricted to 30
	i = 30
	sentence = ""
	while (i>0):
		current_word = nextWord(current_word,bigram_counts)
		sentence = sentence + " " + current_word
		i = i-1
	print sentence

def nextWord(current_word,bigram_counts):
	next_word_score = 0
	next_word = "."
	for item in bigram_counts:
		if (current_word == item) and (item.value > next_word_score):
			next_word_score = item.value
			next_word = item
	return next_word












