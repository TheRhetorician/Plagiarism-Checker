from add_doc import *
import pickle
import os
from calc_tfidf import *

def create_database(docs_path, categories_doc, term_freq_db, doc_freq_db, tf_idf_db):
	'''
	This function creates the database for the plagiarism detector and saves it in pickle format for future use. 
	category_words_docs stores :
	1) The set of words found in the that category
	2) The id number of documents in that category

	id_name stores the name of each file corresponding to their id
	term_freq stores tf for doc x word
	'''

	category_words_docs = {'ML' : [set(), []], 'CG': [set(), []], 'CS':[set(), []], 'IR':[set(), []], 'Business': [set(), []]}
	docs = []
	
	id_name = {}
	for path, category in zip(docs_path, categories_doc):
		category_words = category_words_docs[category][0] 
		curr_id = add_doc(docs, path, category_words,  term_freq_db, doc_freq_db)
		id_name[curr_id] = give_name(path)
		category_words_docs[category][1].append(curr_id)

	try: 
		category_file = open('category_words_docs', 'wb') 
		pickle.dump(category_words_docs, category_file)
		category_file.close()

		id_name_file = open('id_name', 'wb')
		pickle.dump(id_name, id_name_file)
		id_name_file.close() 
		print('Database created successfully')

	except: 
		print("Something went wrong")
	# print(term_freq_db)
	tf_idf_db = calc_tfidf(term_freq_db, doc_freq_db, 2318)

	try : 
		term_freq_db_file = open('term_freq_db', 'wb')
		pickle.dump(term_freq_db, term_freq_db_file)
		term_freq_db_file.close()

		doc_freq_db_file = open('doc_freq_db', 'wb')
		pickle.dump(doc_freq_db, doc_freq_db_file)
		doc_freq_db_file.close()

		tf_idf_db_file = open('tf_idf_db', 'wb')
		pickle.dump(tf_idf_db, tf_idf_db_file)
		tf_idf_db_file.close()

		print("Stonks")

	except :
		print("Something went wrong")

#Extracts name from file path
def give_name(path):
	name = ''
	for i in reversed(path):
		if i != '\\':
			name+=i
		else:
			break
	name = ''.join([i for i in reversed(name)])	
	return name

if __name__ == '__main__':
	categories_doc = ['Business']*2300 + ['CS' ,'IR' , 'IR' , 'ML', 'CS', 'CS', 'IR', 'IR', 'CS', 'IR', 'CS', 'ML', 'ML', 'ML', 'ML', 'CG', 'CG']
	docs_path = []
	for file in range(1,2318):
		file = str(file)+'.txt'
		path = os.path.join(r'.\database', file)
		docs_path.append(path)

	#print(docs_path)
	assert(len(categories_doc)==len(docs_path))
	doc_freq_db = dict()
	term_freq_db = dict()
	tf_idf_db = dict()
	create_database(docs_path, categories_doc, term_freq_db, doc_freq_db, tf_idf_db)	
