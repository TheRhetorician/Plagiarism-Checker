from pre_process import *
from give_docs import *
import pickle
from load_data import *
from create_database import *
from calc_score import *
import operator

category_words_docs, id_name, term_freq_db, doc_freq_db, tf_idf_db = load_data()

def scan_plagiarism(path, category_words_docs, id_name, threshold):
	'''
	Inputs = Path of test document, category_word_docs dictionary, id_name dictionary and threshold for category recognition
	Returns = Top five documents from which plagiarism may have occured and correspondong similarity score  
	'''
	docs, word_freq_doc = give_docs(path, category_words_docs, threshold)
	

	doc = give_name(path)
	words_list = pre_process(path)
	term_freq = dict()

	#Calculating term frequency of test document
	for word in words_list :
		if word in term_freq :
			term_freq[word] += 1
		else :
			term_freq[word] = 1

	print("PLAGIARISM SCORES \n")
	d = calc_score(docs, term_freq, term_freq_db, doc_freq_db, tf_idf_db, 2318)
	d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
	sim_score = dict(list(d.items())[0:10])
	for db_doc in sim_score :
		print(db_doc, sim_score[db_doc])
		print("\n")	

	return sim_score	

if __name__ == '__main__':

	path = r"D:\PYTHON\programs\IR ASSIGNMENT\Plagiarism_Checker\Database\test.txt"
	scan_plagiarism(path, category_words_docs, id_name, 0.5)