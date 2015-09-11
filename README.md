First of all DON'T PANIC.

Here's the breakdown of the code.

**Part I - Import necessary libraries and write some very needed functions.

The first one one is self-explanatory…

The next function is really, really important especially if we are doing text mining with languages 
that have accented characters like Spanish, Portuguese, French, etc.  The issue might not be apparent at first. You have your excel file and all those accented terms look so fancy! Yet, once you try to mess up with your file,  say, simply trying to open the file with Python or R or whatever other language you fancy, you’ll see how nasty it will get.   Instead of “jamón”, you will get “jam/aa2n” and this will make it very hard to to any text mining because you are losing  all the content of the word.  Hence, I decided to remove or replace the accents with their non-accented counterparts – ó = o. Of course, we know that these accents are not purely for decoration, they give meaning to the word, but we have to  trust that the person doing the text mining is fluent in that language. 

The last function we will not use until much later.  Once we have our text mining done, this will print out to the screen the comments containing the topic words.

**Part II - Read and Save Your Data.
What I have done below is separated the file by dropdown value.  So, we will have four different datasets.  Here, I also strip any word that might have an accented character into their non-accented counterpart.  For simplicity, I will only focus of replies with dropdown value = 1. We can then go back to our code and change the dropdown value. 

**Part III - Text Mining
We will be using the library NLTK for the analysis.  
The first thing the code is to tokenize each response. Essentially, a token is a sequence of characters — such as "dog", "cat" — that we want to treat as a group. 

Once the data is in tokens, I count how many words there are.  
Then, I remove all the portuguese 'stopwords', e.g. words like he, she, that, this, and from the remaining words, I only keep the words that appear more than two times in the text.

I then use a bag-of-words algorithm.  The Bag of Words model learns a vocabulary from all of the documents, then models each document by counting the number of times each word appears. For example, consider the following two sentences:

Sentence 1: "The cat sat on the hat"

Sentence 2: "The dog ate the cat and the hat"

From these two sentences, our vocabulary is as follows:

{ the, cat, sat, on, hat, dog, ate, and }

To get our bags of words, we count the number of times each word occurs in each sentence. In Sentence 1, "the" appears twice, and "cat", "sat", "on", and "hat" each appear once, so the feature vector for Sentence 1 is:

{ the, cat, sat, on, hat, dog, ate, and }

Sentence 1: { 2, 1, 1, 1, 1, 0, 0, 0 }

Similarly, the features for Sentence 2 are: { 3, 1, 0, 0, 1, 1, 1, 1}.

With the bag-of-words done, I defined a non-negative matrix factorization to compute the most common topics.  


**Part IV - Deep dive
Lastly, I look a bit more carefully at the common topics by looking at individual frequencies and collocations.
By collocation, I mean pairs of words that are not commonly found together, or statistically interesting pairs of words.

Finally, the code prints out where in the comments where the topics used.
We could do a histogram to visualize the distributions.
