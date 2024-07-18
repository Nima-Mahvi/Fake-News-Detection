import pandas as pd

class pre:
    def preprocess():
        
        true_news = pd.read_csv("true.csv" , encoding = "UTF-8")
        fake_news = pd.read_csv("fake.csv" , encoding = "UTF-8")
        
        true_news["news_text"] = true_news["title"]+ " " + true_news["text"]
        fake_news["news_text"] = fake_news["title"]+ " " + fake_news["text"]
        
        true_news.drop(columns = ["subject", "date", "title", "text"],axis=1,inplace=True)
        fake_news.drop(columns = ["subject", "date", "title", "text"],axis=1,inplace=True)
        
        true_news["target"] = 1
        fake_news["target"] = 0
        
        all_news = pd.concat([true_news , fake_news] , ignore_index=True)
        all_news = all_news.sample(frac = 1, random_state = 38).reset_index(drop = True)
        
        # print(all_news.info())
        # print(all_news["target"].value_counts())
        
        all_news.drop_duplicates(inplace=True)
        # print(all_news.info())
        # print(all_news.describe())
        # print(all_news["target"].value_counts())
        
        all_news.to_csv("NewsData.csv" , index = False)
        print("******  NewsData.csv created successfully!  ******")

        ############################################################################
        
        news = pd.read_csv("NewsData.csv" , encoding="UTF-8")
        
        print("(NewsData.csv) informations: ")
        print(news.info())
        print(news.describe)
        print(news["target"].value_counts())
        print("**********************")
        
        ##############################################################
        
        return news




