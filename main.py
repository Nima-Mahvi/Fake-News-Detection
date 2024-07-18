import pandas as pd
import numpy as np
import time

###########################################
from data_preprocessing import pre
from text_processing import text_process
from NewsScraper import scraper
from modeling import model_selection


## try reading ( NewsData.csv ). if it doesn't exist make it once.
try:
    news = pd.read_csv("NewsData.csv" , encoding="UTF-8")
except:
    data_preprocessing = pre.preprocess()
    news = data_preprocessing
###########################################

## data text processing
data_text_process , labels , vectorizer = text_process.data_text(news)

data = data_text_process
target = labels


# ## just for checking train data & target
# check_data = pd.DataFrame( data.toarray() )
# check = check_data.iloc[:7,:]
# print(" 7 samples of data: " , check)
# print("target: ", target)

###########################################

## This script scrapes news from the BBC website 
## and returns a selected news text for validation.

while True:
    selected_text = scraper.bbc_scrap()
    if selected_text:
        break
    else:
        print("********** \n No news (or text) found. \nPlease select another one. \n **********")
        time.sleep(7)
        
###########################################

## news text processing
test_sample = text_process.test_text_process(selected_text , vectorizer) 

array = test_sample.toarray()
print("The Number of features(words) common between train & test data: ")
print( np.sum(array != 0) )

###########################################

## modeling and prediction
result = model_selection.data_modeling(data , target , test_sample)

# true_news ----> 1
# fake_news ----> 0

if result[0] == 0 :
    print("*********************************")
    print("* The selected news is Fake !!! *")
    print("*********************************")
    
else:
    print("*******************************")
    print("* The selected news is True . *")
    print("*******************************")














