import requests
from clint.arguments import Args
from clint.textui import puts, colored, indent
args = Args()
from pyfiglet import Figlet
f = Figlet(font='slant')
class NewsApi:
    def __init__(self, name):
        self.name = name
    def source(self, source):
        url =  "https://newsapi.org/v2/top-headlines?sources="+ source +"&apiKey=3ce9580385ea4c42a97d1e59537c2f00"
        print(colored.yellow(f.renderText(source)))
        response = requests.get(url)
        json_object = response.json()
        articles = json_object['articles']
        headline = 0
        while headline<10:
            sos = str(articles[headline]['source']['name'])
            x = str(articles[headline]['author'])
            y = str(articles[headline]['title'])
            z = str(articles[headline]['description'])
            pub = str(articles[headline]['publishedAt'])
            q = str(articles[headline]['url'])
            print(colored.yellow("Source:")+ sos + colored.green("\n Title: ")+ y +colored.red("\n Author: ")+ x + colored.blue("\n Description: ") + z + colored.green("\n Url: ")+ q + colored.red("\n Published At: ") + pub)
            print("\n")
            headline+=1    
    def home(self):
        #print(f.renderText('text to render'))
        print(colored.blue(f.renderText("THE NEWS!")))
        print("Hallo "+ self.name +" Welcome to the News Site")
        sources = ["Al-jazeera-english", "Cnn", "Football-italia", "BBc-news"]
        items=1
        for source in sources:
            print(str(items)+":" + source)
            items+=1
        source = input("Enter source number:")
        source_int = int(source)
        if source_int == 1:
            self.source("al-jazeera-english")
        elif source_int == 2:
            self.source("cnn")
        elif source_int == 3:
            self.source("football-italia")
        elif source_int == 4:
            self.source("bbc-news")
        else:
            print("invalid Input")
newsReader = NewsApi("Shamim")
print(newsReader.home())