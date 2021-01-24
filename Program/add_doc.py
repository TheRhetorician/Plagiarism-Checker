from pre_process import *
from create_database import *
	

def add_doc(docs, doc_path, category_words,  term_freq_db, doc_freq_db):
	'''
	Add document in database

	Input : documents in database, path of document, words in the document category,
	word to document index of that category, term_freq_db dictionary

	term_freq_db is a dictionary of dictionaries which stores frequency of each word in every document
	doc_freq_db is a dictionary that stores the id of documents in which the word exists.

	Returns Nothing 
	'''
	curr_id = len(docs)
	docs.append(curr_id)

	curr_word_freq = pre_process(doc_path)  #Word to frequency of document
	doc = give_name(doc_path)
	term_freq_db[doc] = dict()
	for word in curr_word_freq :
		category_words.add(word)
		if word in term_freq_db[doc] :
			term_freq_db[doc][word] += 1
		else :
			term_freq_db[doc][word] = 1

	for word in set(curr_word_freq) :
		if word in doc_freq_db :
			doc_freq_db[word] += 1
		else :
			doc_freq_db[word] = 1
	
	print(f'Added doument {curr_id} to database')
	return curr_id

	

if __name__ == '__main__':
	path = input()
	tech = set()
	add_doc([], path, tech, {}, {})
