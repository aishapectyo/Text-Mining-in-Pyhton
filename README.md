First of all DON'T PANIC.

Here's the breakdown of the code.

Part I - Import necessary libraries and write some very needed functions.
The first one one is self-explanatory…

The next function is really, really important especially if we are doing text mining with languages 
that have accented characters like Spanish, Portuguese, French, etc.  The issue might not be apparent at first.  
You have your excel file and all those accented terms look so fancy! Yet, once you try to mess up with your file, 
say, simply trying to open the file with Python or R or whatever other language you fancy, you’ll see how nasty it will get.  
Instead of “jamón”, you will get “jam/aa2n” and this will make it very hard to to any text mining because you are losing 
all the content of the word.  Hence, I decided to remove or replace the accents with their non-accented counterparts – ó = o. 
Of course, we know that these accents are not purely for decoration, they give meaning to the word, but we have to 
trust that the person doing the text mining is fluent in that language. 

The last function we will not use until much later.  
Once we have our text mining done, this will print out to the screen the comments containing the topic words.


Part II - Read and Save Your Data.
