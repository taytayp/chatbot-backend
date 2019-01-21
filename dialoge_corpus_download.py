import nltk
import time

nltk.download('nps_chat')
from nltk.corpus import nps_chat

for i in nps_chat.words():
    print(i)
    time.sleep(.5)
