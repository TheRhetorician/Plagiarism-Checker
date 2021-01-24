from pre_process import *
from create_database import *

def give_docs(path, category_words_docs, threshold):
	'''
	Gives the category of a document given word_freq of that document.

	Inputs : path of document, category_words_docs, threshold (Intersection ratio)

	word_freq_doc has frequency of words in the document
	category_words_docs is a dictionary that stores set of words in a category and list of documents of that category, for every category in the database 

	prints probable categories of document

	Returns : List docs, word_freq_doc 
	'''
	processed_doc = pre_process(path)
	word_freq_doc = generate_word_freq(processed_doc)
	words = set([word for word in word_freq_doc])
	docs = []
	categories = []
	for category in category_words_docs:
		intersection_ratio = len(words.intersection(category_words_docs[category][0]))/len(words)
		print(f'Intersection ratio with {category} is {intersection_ratio}')
		if intersection_ratio>=threshold:
			categories.append(category)
			docs.append((category_words_docs[category][1], category))
	print(f'Document belongs to {categories} category')
	return docs, word_freq_doc

	
def generate_word_freq(processed_doc):
	'''
	Generates word_freq of the document
	'''
	word_freq_doc = dict()
	for word in processed_doc:
		if word in word_freq_doc:
			word_freq_doc[word] += 1
		else:
			word_freq_doc[word] = 1

	return word_freq_doc

if __name__ == '__main__':
	import pickle 
	file = open('category_words_docs','rb')
	category_words_docs = pickle.load(file)
	file.close()
	docs, word_freq_doc = give_docs(r'D:\PYTHON\programs\IR ASSIGNMENT\Plagiarism_Checker\Database\15.txt', category_words_docs, 0.5)
