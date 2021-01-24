import math
import copy 
# assuming a term frequency dictionary for all documents term_freq (document x word)  

#assuming a document frequency dictionary for all words doc_freq (storing number of occurances of a word across all documents)
#the number of documents in the collection that contain the word

#assuming N number of documents preprocessed

def calc_tfidf(term_freq, doc_freq, N) :
	'''
	returns tf_idf for all documents x words
	using logarithmic normalization in tf_idf(t,d) = tf(t,d)*idf(t)
	where idf(t) = log(N / df(t)) and
	tf_idf = (1+log(tf)) / (1+idf)
	temp values in tf_idf
	'''
	tf_idf = copy.deepcopy(term_freq)
	for dno in tf_idf :
		for term in tf_idf[dno] :
			multiplicand1 = math.log(term_freq[dno][term]) # sublinear term_freq scaling
			multiplicand1 += 1
			multiplicand2 = math.log(N / doc_freq[term]) 
			multiplicand2 += 1
			tf_idf[dno][term] = multiplicand1 * multiplicand2
	return tf_idf
