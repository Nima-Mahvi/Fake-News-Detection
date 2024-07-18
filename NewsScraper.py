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
        
        
        # Extract all links within the specified div structure
        divs = soup.find_all('div', class_="sc-9c1d76a2-2 fVwEgN")
        
        links = {}
        cnt=0
        numbers=set()
        for div in divs:
            link_tags = div.find_all('a', href=True)
            if link_tags :
                cnt+=1
                numbers.add(cnt)
                for tag in link_tags:
                    links[cnt] = tag['href']
        # print("links found: ", links)
        
        for cnt , link in links.items():
            url = "https://www.bbc.com"+link
            print(cnt ,")" ,"\n","url: " , url ,"\n")
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content , "html.parser")
                article = soup.find('article')
                if article:
                    text = article.get_text(separator = "\n")
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
        
            
        
        
        