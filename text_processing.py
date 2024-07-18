from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import warnings
import string
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')


class text_process:
    
    def data_text(news):
        
        def clean_text(text):
            text = text.lower()
            text = re.sub(r'\d+', '', text)
            text = re.sub(r'[^\w\s]', '', text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text
        
        def remove_stopwords(text):
            tokens = word_tokenize(text)
            tokens = [word for word in tokens if word not in stop_words]
            return ' '.join(tokens)
        
        def lemmatize_text(text):
            tokens = word_tokenize(text)
            tokens = [lemmatizer.lemmatize(word) for word in tokens]
            return ' '.join(tokens)
        
        print("Please wait for a while as the Data text processing steps are completed! ")
        print("Data Loading...")
        
        news['news_text'] = news['news_text'].apply(clean_text)
        
        stop_words = set(stopwords.words('english'))
        news['news_text'] = news['news_text'].apply(remove_stopwords)
        
        lemmatizer = WordNetLemmatizer()
        news['news_text'] = news['news_text'].apply(lemmatize_text)
        
        
        vectorizer = TfidfVectorizer(max_features=7000)
        vectors = vectorizer.fit_transform(news["news_text"])
        features = vectors
        # print(vectors.shape)
        
        labels = news["target"]
                
        return features , labels , vectorizer

#################################################################

    def test_text_process(selected_text , vectorizer):
        
        def text_process(text):

            text = text.translate(str.maketrans('', '', string.punctuation))
            text = [word for word in text.split() if word.lower() not in stopwords.words('english')]

            return " ".join(text)

        new_text = text_process(selected_text)
        print("text without stopwords: \n \n" , new_text)
        # print(len(new_text.split()))
        print("*************************")

        words = word_tokenize(new_text)
        print("words in text: \n \n" , words)
        print("*************************")
        print("number of words in text: \n" , len(words))
        print("*************************")

        lemmatizer = WordNetLemmatizer()

        lemmatized_words = []

        for word in words:
            lemmatized_words.append(lemmatizer.lemmatize(word.lower() , "v"))

        # print(type(lemmatized_words))
        # print("lemmatized: ",len(lemmatized_words))

        fd_lemmatized = FreqDist(lemmatized_words)
        # print(fd)
        print("30 common words in text: \n",fd_lemmatized.most_common(30))
        fd_lemmatized.plot(40 , cumulative=False)
        plt.show()
        print("*************************")

        ## Creating a corpus of test text :
        test_text = ""
        for word in lemmatized_words:
                test_text = test_text + word + " "

        # print(test_text)

        vectors = vectorizer.transform([test_text])
        test_features = vectors

        print("test text sample shape: " ,test_features.shape)
        
        return test_features






























