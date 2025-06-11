def get_text_words(text):
	words = text.split()
	word_count = len(words)
	return word_count
def get_text(texts):
	if not texts: 
		return None
	
	dic_texts = {}
	for text in texts.lower():
		if  text in dic_texts:
			dic_texts[text] += 1 
		else:
			dic_texts[text] = 1
	return dic_texts
			 
def sort_on(dic_texts):
        return dic_texts["num"]

letter_count = {'e': 44538, 'a': 200}
counter_list = []
for key, value in letter_count.items():
	counter_list.append({"char": key, "num": value})
counter_list.sort(reverse=True, key=sort_on)

print(counter_list)
