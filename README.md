# Fake-News-Detection
This project aims to detect fake or real news on the BBC website using various technologies and algorithms.
It processes and analyzes news articles from BBC News to distinguish between factual and misleading information.

## Project Overview:

1. **Data Preprocessing**: Reading datasets containing fake and true news articles, preprocessing the data, and combining them into a single CSV file.
2. **Text Processing**: Cleaning the text within the dataset and converting key terms into features for machine learning operations.
3. **BBC Website Scraping**: Fetching several news articles from the BBC website and allowing the user to select one for evaluation.
4. **Processing User-Selected News Text**: Preparing the news text selected by the user for evaluation.
5. **Modeling and Prediction**: Initially modeling with two different algorithms to determine which gives better results, then evaluating and predicting the test sample.

## Technologies and Libraries Used:

- **Programming Language**: Python
- **Libraries**:
  - NumPy
  - Pandas
  - NLTK
  - BeautifulSoup
  - Requests
  - Scikit-learn
  - Matplotlib
  - Time
  - re
  - Warnings
  - String
- **Algorithms**:
  - Naive Bayes
  - Logistic Regression

## Usage:

To use this project, follow these steps:

1. **Ensure Internet Connection**: Ensure a stable internet connection as the texts need to be scraped from the BBC website.
2. **Run**: Run the main.py file and wait for the processes to complete.
3. **Select News Article**: Choose one of the suggested news articles with text for evaluation.
4. **View Results**: Results can be viewed in the console. Besides identifying the news as fake or real, additional information such as the number of words, most frequent words with their charts, the number of common features (or words) between the test and training data, and more will be displayed.

**Note**: Although this model has relatively high accuracy (trained with 70% of the data and predicted with 98% accuracy on the remaining 30%), there is no guarantee of entirely accurate detection due to uncertainties in data quality downloaded from the internet and the accuracy of news labels in this data, which have not been validated. The purpose of this project is solely to utilize programming skills.

Feel free to customize or expand upon this project. If you have any questions or need further assistance, please don't hesitate to reach out!
