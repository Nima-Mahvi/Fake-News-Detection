from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class model_selection:
    def data_modeling(data , target , test_sample):
        
        X_train, X_test, y_train, y_test = train_test_split(data , target ,
                                                            test_size=0.3,
                                                            random_state=111)
        
        # ############# Multinomial Naive Bayes   Accuracy ( ~0.94 )
        # mnb = MultinomialNB()
        # mnb.fit(X_train,y_train)
        
        # # # Prediction
        # y_pred = mnb.predict(X_test)
        
        # # # Accuracy
        # print("Accuracy: " , accuracy_score(y_test, y_pred))
        # conf_matrix = confusion_matrix(y_test, y_pred)
        # print("confusion_matrix: \n" , conf_matrix)
        
        # ############## logistic regression   Accuracy ( ~0.99 )
        # logreg=LogisticRegression()
        # logreg.fit(X_train,y_train)
        
        # y_pred = logreg.predict(X_test)
        
        # # Accuracy
        # print("Accuracy: " ,logreg.score(X_test, y_test))
        # conf_matrix = confusion_matrix(y_test, y_pred)
        # print("confusion_matrix: \n" ,conf_matrix)
        
        ''' logistic regression is more accurate and better for training
        but Multinomial Naive Bayes has lower cost and may be faster
        However,I selected the logistic regression for the modeling '''
        
        ## now we can use our 100% data for better trainnig

        logreg=LogisticRegression()
        logreg.fit(data , target)
        y_pred = logreg.predict(test_sample)
        
        return y_pred
        
        
        























