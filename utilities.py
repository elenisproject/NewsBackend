#------------------------               DESCRIPTION                 ----------------------------------
#this file contains all the funtions used in other files
#-----------------------------------------------------------------------------------------------------

import pandas as pd
import unicodedata
import re
import string
import json
import itertools
import statistics 
from joblib import Parallel, delayed
import collections
import mysql.connector  
from collections import Counter,defaultdict,OrderedDict,namedtuple
from settings import DB_CREDS,categories


#establish connection with database
cnx = mysql.connector.connect(
    host = DB_CREDS['host'],
    user = DB_CREDS['user'],
    passwd = DB_CREDS['pass'],
    database = DB_CREDS['db']   
)

#make all small function
def removeAccents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return (u"".join([c for c in nfkd_form if not unicodedata.combining(c)])).lower()

#keep all small words
def normalize (i):
    all_small = removeAccents(i)
    split_to_tokens = re.findall(r'[α-ω]+',all_small)
    return(split_to_tokens)

def finalNormalize (i):
    text = normalize(i)
    f = open("dependencies/filter_words.txt", "r")
    f.readline()
    stop_words=f.readline()
    short_words=f.readline()
    f.close()
    f = open("dependencies/imported_stop_words.txt", "r")
    fix_words=f.readline()
    f.close()
    filtered_sentence = list(filter(lambda i: i not in stop_words, text))
    second_filter = list(filter(lambda i: i not in short_words, filtered_sentence))
    third_filter = list(filter(lambda i: i not in fix_words, second_filter))
    return(third_filter)

def uselessWords(input_str):
    #combine all the words from every article and to it parallel
    all_words = Parallel(n_jobs=-1, backend="loky")(map(delayed(normalize), input_str))

    #put them in one list
    all_articles_combined = list(itertools.chain.from_iterable(all_words))

    #find the shortest in length
    short_words = sorted(list(set(all_articles_combined)),key=len)
    short = short_words[0:500]

    #find the 118 most commonly used words
    most_common_words = Counter(all_articles_combined).most_common(300)

    #keep the most common words    
    stop_words = []
    for i in most_common_words:
        stop_words.append(i[0])
    
    return (stop_words,short)

def SortMyDict(df,index):

    #fill all null values in the table
    df = df.fillna(" ")

    #create empty dictionary
    my_dict = {k:0 for k in df.index}

    #this will be the set o words from our input
    setA = set((df.at[index,'article_body']).split())

    #get intersection for this for all the articles from our data
    for x in df.index:
        setB = set((df.at[x,'article_body']).split())
        my_dict.update({x:len(setA.intersection(setB))})

    sort_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    return (sort_dict)

#read function
def readText(i):
    df = pd.read_sql(i, con=cnx)
    return (df)

#write funtion
def WriteData (out_file,text):
    fname = out_file
    with open(fname, 'a+') as f:
        f.write('\n')
        f.write(text)


#write to cell function
def WriteCell(my_id,keys):
    connection = cnx 
    mySql_insert_query = """INSERT INTO similar_articles (id,first_article,second_article,third_article,fourth_article,fifth_article) 
                           VALUES 
                           (%s,%s,%s,%s,%s,%s)
                            """
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query,(my_id,keys[0],keys[1],keys[2],keys[3],keys[4]))
    connection.commit()
    cursor.close()


#function that gets as input text and returns a dict with the 100 most popular ones
def FindTop(articles):
    #initiate an empty list to save all the words of all the articles
    all_words_compined = []
    
    for words in articles:
        #split the articles to words
        word_list = words.split()
        #save the words to our list
        all_words_compined.extend(word_list)
        
    #find the 500 most common
    top = Counter(all_words_compined).most_common(2000)
    return top

def CombineArticles(category,df):
    culture_articles = df.groupby(['topic']).get_group(category)['article_body']
    #set an empty variable to save all the words 
    category_words_combined = []

    #combine all words from each article
    for words in culture_articles:
        word_list = words.split()
        category_words_combined.extend(word_list) 
    
    return(category_words_combined)

#shuffle data and splint in 70%, 30% for testing

#main tester
def MainTester(all_categories):
    df2 = pd.read_csv('/Users/elenikaranikola/Desktop/NewsBackend/output.csv', index_col='id')
    df2 = df2.fillna(" ")

    max = 0
    sum = 0
    correct_category = 0
    wrong_category = 0
    for x in df2.index:
        article = df2.at[x,'article_body'] 
        input_to_tokens = set(article.split())

        for category in all_categories:

            for i in input_to_tokens:
                if i in all_categories[category]:
                    sum += all_categories[category][i]
            if max < sum :
                max = sum
                final_category = category
        if final_category == df2.at[x,'topic']:
            correct_category += 1
        else:
            wrong_category += 1


    final_res = correct_category/wrong_category * 100
    return (final_res)

#def that returns the prediction
def Predictor(my_input,all_categories):
    max = 0
    final_category = ' '
    input_to_tokens = set(my_input)
    for category in all_categories:
        sum = 0
        for i in input_to_tokens:
            if i in all_categories[category]:
                sum += all_categories[category][i]
        if max < sum :
            max = sum
            final_category = category

    return (final_category)


def finalNormalizeFullPath(i):
    text = normalize(i)
    f = open("/Users/elenikaranikola/Desktop/NewsBackend/dependencies/filter_words.txt", "r")
    f.readline()
    stop_words=f.readline()
    short_words=f.readline()
    f.close()
    f = open("/Users/elenikaranikola/Desktop/NewsBackend/dependencies/imported_stop_words.txt", "r")
    fix_words=f.readline()
    f.close()
    filtered_sentence = list(filter(lambda i: i not in stop_words, text))
    second_filter = list(filter(lambda i: i not in short_words, filtered_sentence))
    third_filter = list(filter(lambda i: i not in fix_words, second_filter))
    return(third_filter)

def FindTopTester(articles,top_words):
    #initiate an empty list to save all the words of all the articles
    all_words_compined = []
    
    for words in articles:
        #split the articles to words
        word_list = words.split()
        #save the words to our list
        all_words_compined.extend(word_list)
        
    #find the 500 most common
    top = Counter(all_words_compined).most_common(top_words)
    return top

def ClassifierTester(cleaned_output,top_words,df):          
    articles = list(cleaned_output['article_body'])  
    top_x_words = FindTopTester(articles,top_words)       

    words_dict = {}

    #from the list of words create a dictionary with key the word and value the times we counted it in all our data
    for word in top_x_words:
        words_dict[word[0]]=word[1]

    all_categories = {}

    #for each category combine all its articles words
    #and calculate the percent of appearance based on the top 100 words
    #and save in a new dict with key the category and value another dict with key the word and value the percentage
    for category in categories:
        category_words_combined = CombineArticles(category,df)
        sub_dict = {}
        cnt = Counter(category_words_combined)

        for word in words_dict:
            persentage = cnt[word] / words_dict[word]
            sub_dict[word] = persentage

        all_categories[category] = sub_dict

    return(all_categories)