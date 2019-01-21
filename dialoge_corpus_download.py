import nltk
import time

nltk.download('nps_chat')
from nltk.corpus import nps_chat

for i in nps_chat.words():
    print("Raw word: " + i)
    token = nltk.word_tokenize(i)[0]
    print("Token: " + token)
    print("---")
    time.sleep(.5)
