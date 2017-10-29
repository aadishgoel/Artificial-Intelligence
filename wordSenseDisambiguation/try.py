from nltk.tokenize import word_tokenize
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
import pywsd.lesk as wsd

#s = 'I went to the bank to deposit money.', 'I was walking around a river bank while looking at fishes in the water.'
#s = [ 'willows lined the bank of the stream' ]
#s= [ 'a bank account has 30 thousand rupees' ]

#s = ['I take my car in a parking lot and park it there.']
#s = ['Park is filled with trees and childrens play cricket in it']

ambiguous = 'bank'
#ambiguous = 'park'

for fn in [lesk, wsd.original_lesk, wsd.simple_lesk, wsd.adapted_lesk, wsd.cosine_lesk]:
    for sent in s:
        #words = word_tokenize(sent)
        ans = fn(sent,ambiguous)
        print(ans,ans.definition() if ans else 'Not Found')
    print()
'''
for i in wn.synsets('bank'):
    print(i)
'''
