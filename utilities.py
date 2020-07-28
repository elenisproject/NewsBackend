#------------------------               DESCRIPTION                 ----------------------------------
#in this python file we find and extract the most common words in the given file
#the extracted data are being saved in settings.py
#-----------------------------------------------------------------------------------------------------

import pandas as pd
import unicodedata
import re
import string
import json
import itertools
from joblib import Parallel, delayed
import collections
import mysql.connector  
from collections import Counter,defaultdict,OrderedDict,namedtuple
from settings import DB_CREDS

fname = 'settings.py'

#establish connection with database
cnx = mysql.connector.connect(
    host = DB_CREDS['host'],
    user = DB_CREDS['user'],
    passwd = DB_CREDS['pass'],
    database = DB_CREDS['db']   
)

#get all data
df = pd.read_sql('SELECT * FROM articles', con=cnx)

#save in the text variable tha articles body
text = df['article_body']

#make all small function
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return (u"".join([c for c in nfkd_form if not unicodedata.combining(c)])).lower()

#keep all small words
def normalize (i):
    all_small = remove_accents(i)
    split_to_tokens = re.findall(r'[α-ω]+',all_small)
    return(split_to_tokens)

def final_normalize(input_str):
    #combine all the words from every article and to it parallel
    all_words = Parallel(n_jobs=-1, backend="multiprocessing")(map(delayed(normalize), input_str))

    #put them in one list
    all_articles_combined = list(itertools.chain.from_iterable(all_words))

    #find the shortest in length
    #short_words = [set(sorted(all_articles_combined,reverse=True,key=len))]
    short_words = sorted(list(set(all_articles_combined)),key=len)
    short = short_words[:200]

    #find the 118 most commonly used words
    most_common_words = Counter(all_articles_combined).most_common(118)

    #keep the most common words    
    stop_words = []
    for i in most_common_words:
        stop_words.append(i[0])
    
    return (stop_words,short)

#normalize the extracted data
file_data = final_normalize(text)
data1 = file_data[0]
data2 = file_data[1]

#write our extracted data in most_common_words.py
with open(fname, 'a+') as f:
    f.write('\n')
    f.write('stop_words = set({})'.format(data1))
    f.write('\n')
    f.write('short_words = set({})'.format(data2))