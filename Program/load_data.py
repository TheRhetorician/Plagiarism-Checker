import pickle

def load_data():
	'''
	Loads files from the database
	'''

	with open('category_words_docs', 'rb') as f:
	    category_words_docs = pickle.load(f)
	
	file = open('term_freq_db','rb')
	term_freq_db = pickle.load(file)
	file.close()

	file = open('doc_freq_db','rb')
	doc_freq_db = pickle.load(file)
	file.close()	

	file = open('tf_idf_db','rb')
	tf_idf_db = pickle.load(file)
	file.close()

	with open('id_name', 'rb') as f:
	    id_name = pickle.load(f)

	return category_words_docs, id_name, term_freq_db, doc_freq_db, tf_idf_db
