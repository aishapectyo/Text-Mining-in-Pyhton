#!/usr/bin/env python/

"""
Text MIning Algorithm. Portuguese specific - easy to modify for other languages.
By: Aisha Mahmoud-Perez
Date: September 10, 2015

"""

#---Import necessary libraries---#
import sys
import os
import numpy as np
import string
import matplotlib as plt
import unicodedata
import csv
import nltk
from nltk.text import Text
from nltk.probability import FreqDist

#---Functions---#
def check_file(data_file):
	"""Check if file exists. If file exists, load and parse the data file. """
	if os.path.isfile(data_file):
		return "File exists. Loading data nto individual arrays..."
	else:
		return "Program will crash... check file name and/or location."

def strip_accents(s):
	"Remove those little naughty, pain-giving accents from Spanish and/or Portuguese!"
	return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn') 
	
def get_all_phrases_containing_tar_wrd(target_word, tar_passage, left_margin = 20, right_margin = 20):
	"Print all comments showing the input keywords"
	tokens = nltk.word_tokenize(tar_passage)
	text = nltk.Text(tokens)
	c = nltk.ConcordanceIndex(text.tokens, key = lambda s: s.lower())
	concordance_txt = ([text.tokens[map(lambda x: x-5 if (x-left_margin)>0 else 0,[offset])[0]:offset+right_margin]  for offset in c.offsets(target_word)])
	return [''.join([x+' ' for x in con_sub]) for con_sub in concordance_txt]

#---Main---#
#Read data.
filename = "GeCAESpt.csv"
replies_1=[] #these are empty arrays to store your data.
replies_2=[]
replies_3=[]
replies_4=[]

with open(filename,'r') as f: #open csv file.
	header_line = next(f)
	reader = csv.reader(f, delimiter= ',')
	for row in reader: #for each row in your file, check what the dropdown value is, and save into a variable.
		if row[6] == '1':
			item = row[8].decode("unicode-escape") #change to unicode.
			stripped = strip_accents(item) #strip of accents.
			replies_1.append(stripped)
		if row[6] == '2':
			item = row[8].decode("unicode-escape")
			stripped = strip_accents(item)
			replies_2.append(stripped)
		if row[6] == '3':
			item = row[8].decode("unicode-escape")
			stripped = strip_accents(item)
			replies_3.append(stripped)
		if row[6] == '4':
			item = row[8].decode("unicode-escape")
			stripped = strip_accents(item)
			replies_4.append(stripped)

print("\n")
print("#############################################################################")
print("# Get up and dance because your data was cleaned succesfully! #Slay #Yaaas!")
print("#############################################################################")
print("\n")		
#---Text Mining---#
#---->Initial Exploration

#Tokenize all your data.
#E.g. "This is a sentence" - "This", "is", "a", "sentence"
tokenized= []
replies_len = len(replies_1) #*****************change dropdown value here
for reply in xrange(replies_len):
	lower = string.lower(replies_1[reply]) #*****************change dropdown value here
	tokenized.append(nltk.word_tokenize(replies_1[reply])) #*****************change dropdown value here

#Merge your data.
i = 0
initial= tokenized[0]
eol = len(tokenized)
while i < eol:
	all_words = initial +tokenized[i]
	initial_1 = all_words
	i = i + 1

#Select all the 'unique' words.
len(set(all_words))

# Change the ordering of value and key for sorting
items = [(v, k) for k, v in wordcounts.items()]

# Count the occurences of all words
wordcounts = dict([ [t, all_words.count(t)] for t in set(all_words) ])

for count, word in sorted(items, reverse=True)[:5]:
    print("%5d %s" % (count, word))

# Filter out common words
stopwords = nltk.corpus.stopwords.words("portuguese")
terms = {}

#Select via frequency and non-stopwords.
for word, count in wordcounts.iteritems():
    if count > 2 and word not in stopwords and word.isalpha():
        terms[word] = count
        
# Change the ordering of value and key for sorting
items = [(v, k) for k, v in terms.items()]

for count, word in sorted(items, reverse=True)[:5]:
    print("%5d %s" % (count, word))
    
# Convert the dictionary to a list.
terms = list(terms)

#Create a bag-of-words matrix
M = np.asmatrix(np.zeros([len(tokenized), len(terms)]))
terms_len = len(terms)
for n in xrange(eol):
	for m  in xrange(terms_len):
		M[n,m] = tokenized[n].count(terms[m])

# Define a topic mining function (non-negative matrix factorization)
def nmf(M, components=5, iterations=5000):
    # Initialize to matrices
    W = np.asmatrix(np.random.random(([M.shape[0], components])))
    H = np.asmatrix(np.random.random(([components, M.shape[1]])))
    for n in range(0, iterations): 
        H = np.multiply(H, (W.T * M) / (W.T * W * H + 0.001))
        W = np.multiply(W, (M * H.T) / (W * (H * H.T) + 0.001))
        print "%d/%d" % (n, iterations)    # Note 'logging' module
    return (W, H)

# Perform the actual computation
W, H = nmf(M, iterations=50, components=3)
# Show the results in some format
for component in range(W.shape[1]):
    print("="*80)
    print("COMPONENT %d: " % (component,))
    indices = (-H[component,:]).getA1().argsort()
    print(" - ".join([ terms[i] for i in indices[:6] ]))
    print("-")
    indices = (-W[:,component]).getA1().argsort()

#----->Deep dive
#Frequency distributions
sorted(items, reverse = True)
fdist1 = FreqDist(all_words)
sorted(w for w in set(all_words) if len(w) > 7 and fdist1[w] > 7)

#Look at collocations: A collocation is a sequence of words that occur together unusually often.
text = nltk.Text(all_words) 
text.collocations()

#Explore where in the text these keywords appear.
print("\n")
tarwrd = 'antigo'
print("****Looking at specific words in the corpus... In this case, I chose the word ", tarwrd)
replies_merged = ', '.join([x for x in replies_1]) #*****************change dropdown value here
replies_merged = string.lower(replies_merged) 
replies_merged=unicodedata.normalize('NFKD', replies_merged).encode('ascii','ignore')
results = get_all_phrases_containing_tar_wrd(tarwrd, replies_merged)
for result in results:
    print result
