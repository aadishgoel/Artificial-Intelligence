from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import pywsd

#p = input() 
p = 'I was walking around a river bank while looking at fishes in the water.'

new= [ word for word in word_tokenize(p) if word not in stopwords.words('English') and word not in string.punctuation]
new = ' '.join(new)
for word, context in pywsd.disambiguate(new):
    print(word.ljust(15,' '),':  ' ,context.definition() if context else 'Not Found' )


