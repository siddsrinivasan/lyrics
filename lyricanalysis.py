import csv
import nltk
import lyricalfunctions as lf


filename = "songdata.csv"

## Script
data = []

with open(filename) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		data.append(row)


#contains unique set of artists
list_of_artists = []
for entry in data:
	artist = entry["artist"]
	if artist not in list_of_artists:
		list_of_artists.append(artist)

name = input("Input an Artists name to prompt artifical sentence generation\n")

# Ensure user has valid input.
while name not in list_of_artists:
	name = input("Unfortunately we don't have songs on record for this artist, please input another artist \n")

text = []
for entry in data:
	if entry["artist"] == artist:
		text.append(entry["text"])

#preprocess the text
text = lf.cleanUp(text)
unigram_counts = lf.unigramCounts(text)
bigram_counts = lf.bigramCounts(text)

lf.makeSentence(text,unigram_counts,bigram_counts)








