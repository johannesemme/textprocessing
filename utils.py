import re
import collections

def word_search(text, searchwords):
    searchwords = [w.lower() for w in searchwords]
    text = re.sub('[^A-ZÆØÅa-zæøå0-9]+', ' ', text) # remove special characters
    textcount = collections.Counter(text.lower().split(" ")) # get count dict for text
    
    d = {}
    for word in searchwords: # loop through words and get count wrt. text
        cnt = textcount.get(word, 0)
        d[word] = cnt
    
    return d


def file_read(folder, filename, searchwords):
    with open(folder + filename, "r", encoding="utf-8") as f:
        d = word_search(f.read(), searchwords)
    return filename, d