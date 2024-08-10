import requests
from bs4 import BeautifulSoup

class scraper:
    def bbc_scrap():
        ## requesting the website
        url = "https://www.bbc.com/news/world/europe"

        response = requests.get(url)
        # print("the response code is : ",response)

        ## parese the HTML document
        soup = BeautifulSoup(response.content , "html.parser")


        # Extract all links 
        divs = soup.find_all('div')

        links = {}
        cnt=0
        for div in divs:
            link_tags = div.find_all('a', href=True)
            if link_tags :
                cnt+=1
                for tag in link_tags:
                    links[cnt] = tag['href']
        
        print("------------------------------------")
        print("links found: \n", links)
        print("------------------------------------")

        # Extract 5 links with text containing fewer than 700 words 
        # and identify any duplicate articles for removal.

        counter=0
        numbers=set()
        check_duplicates=set()
        for cnt , link in list(links.items())[40:]:
            if counter >=5:
                break
            
            url = "https://www.bbc.com"+link
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content , "html.parser")
                article = soup.find('article')
                if article:
                    text = article.get_text(separator = "\n")
                    words_in = len(text.split())
                    if words_in < 700 and words_in not in check_duplicates:
                            check_duplicates.add(words_in)
                            counter+=1
                            numbers.add(cnt)
                            print(cnt ,")" ,"\n","url: " , url ,"\n")
                            print(text)
                            print("--------------------------- \n \n")
            except:
                continue
           
        print(numbers)
        ## choose a news
        while True:
                selected = int(input("\n Please select one of the news numbers (that have text) for validation : "))
                if selected in numbers:
                    selected_link = links[selected]
                    break
                else:
                    print("The entered number is incorrect!") 
        try:    
            main_url = "https://www.bbc.com"+selected_link
            print("user selection: " , main_url)
            
            response = requests.get(main_url)
            soup = BeautifulSoup(response.content , "html.parser")
            
            article = soup.find('article')
            if article:
                text = article.get_text(separator = "\n")
                print(text)
                print("--------------------------- \n \n")
                
                return text
            
        except:
            text = False
            
            return text
        
