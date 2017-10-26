from nltk.tokenize import word_tokenize
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn


#sentences = 'I went to the bank to deposit money.', 'I was walking around a river bank while looking at fishes in the water.'
sentences = 'I park my car in the parking area of an appartment.', 'We go to park daily for jogging.'


for sent in sentences:
    words = word_tokenize(sent)
    ans = lesk(words,'park')
    print(ans,ans.definition())

'''
for i in wn.synsets('bank'):
    print(i)
'''
