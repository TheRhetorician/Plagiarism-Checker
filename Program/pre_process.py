import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
# nltk.download('stopwords')

def pre_process(path):
	'''
	tokenizer tonkenizes words and they are stored in a list of words including stop words . Punctuations are also removed.
	Removes stop words , stems and changes to lowercase 
	'''
	ps=PorterStemmer()
	stop_words=set(stopwords.words("english"))
	with open(path, 'r', encoding = 'latin1') as f:
		contents = f.read()

	#tokenizer tonkenizes words and they are stored in words including stop words . Punctuations are also removed.
	tokenizer = RegexpTokenizer(r'\w+')
	words = tokenizer.tokenize(contents)

	#removes stop words , stems and changes to lowercase 
	filtered_sentence = []
	for w in words:
	    if w not in stop_words:
	        filtered_sentence.append(ps.stem(w.lower())) #stems and lowers
	
	return filtered_sentence



