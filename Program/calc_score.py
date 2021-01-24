import math
import copy
import pickle
def calc_score(docs,term_freq, term_freq_db, doc_freq_db, tf_idf_db, N) :
	'''
	Inputs - 
	test_doc is the document to be tested
	a term frequency dictionary for all documents term_freq_db (document x word) 
	assuming a document frequency dictionary for all words doc_freq_db (storing number of occurances of a word across all documents)
	the number of documents in the collection that contain the word
	assuming tf_idf_db is tf_idf for entire database
	N is number of documents in db
	returns cosine similarity score
	term_freq(words) has frequency of all words in the test_doc
	call to fn calculating term_freq for test_doc after processing the doc using GUI function
	tf_idf(words) stores tf_idf for test_doc (only corresponding to the words in the test_doc not the entire db)

	Outputs - 
	similarity score between test document and category documents
	'''
	file = open('id_name','rb')
	id_name = pickle.load(file)
	file.close()
	tf_idf = copy.deepcopy(term_freq)

	for doc in tf_idf_db :
		for term in tf_idf_db[doc] :
			if term in term_freq :

				multiplicand1 = math.log(term_freq[term])
				multiplicand1 += 1
				multiplicand2 = math.log(N / doc_freq_db[term])
				multiplicand2 += 1

				tf_idf[term] = multiplicand1 * multiplicand2

	score = dict()
	# score(doc) = (VecA . VecB) / (mag(VecA) x mag(VecB))
	# VecA is tf_idf value for term in test_doc
	# VecB is tf_idf value for term in db
	for document in docs :
		for dn in document[0] :
			dno = id_name[dn]
			vecA = 0 #store mag of test doc
			vecB = 0 #store mag of db docs

			score[dno] = 0

			#calc mag of test doc and cos product/score
			for term in term_freq :
				if term in term_freq_db[dno] :
					temp = tf_idf_db[dno][term] * tf_idf[term]
					score[dno] = score[dno] + temp

				vecA += math.pow(tf_idf[term],2)

			#calc mag of db docs
			for term in term_freq_db[dno] :
				vecB += math.pow(tf_idf_db[dno][term],2)

			temp = math.sqrt(vecA) * math.sqrt(vecB)
			score[dno] = score[dno] / temp
	for doc in score :
		score[doc] = score[doc] * 100
		score[doc] = round(score[doc],2)
	return score