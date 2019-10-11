import operator

word_count = {}
words = []
with open('word_search.tsv') as dataset: 				
	for row in dataset:
		word, frequency = row.split('\t') 			        #splitting it into word and occurence frequency
		word_count[word] = int(frequency.strip())	        #inserting into the wordcount dictionary key as word and value as frequency
		words.append(word)

#Search method to check the input word (partial) is present in any word of words from dataset
def search(word_letter):
	result = []
	for word in words:
		if word_letter in word:
			result.append(word)
	return result

#    This part sorts the words based on a match with the search keyword.
# 1. Matches at the start of a word ranks higher.
# 2. Common words (those with a higher usage count) ranks higher than rare words.
# 3. Short words ranks higher than long words.
# 4. An exact match always ranks as the first result.
def sort(results, incomplete_word):
	result_a = [(result, result.find(incomplete_word), word_count[result], len(result)) for result in results]
	#result_a.sort(key=operator.itemgetter(2))
	result_a.sort(key=operator.itemgetter(1))
	result_a.sort(key=operator.itemgetter(3))
	
	#print(result_a)
	searchResults = [result_distance[0] for result_distance in result_a][:25]
	
	#print(searchResults)
	return searchResults

