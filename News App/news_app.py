from tkinter import *
from selenium import webdriver
import time,json,requests
from tkinter import messagebox

class News(Frame):
    def __init__(self, parent): 
        Frame.__init__(self, parent)
        self.parent = parent 
        self.news=[]
        self.initUI()
    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        self.lb = Listbox(self, selectmode="single",width=150,height=10)
        self.scrollbar=Scrollbar(self)
        self.scrollbar.pack(side = RIGHT, fill = BOTH)
        self.lb.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.lb.yview)
        bring_btn = Button(self,text="Bring the News", command=self.bring_the_news)
        go_to_news_btn = Button(self, text="Go To News",command=self.go_to_news)
        create_json_btn = Button(self, text="Create the News Json File",command=self.create_the_json)
        self.lb.pack(expand=True, fill=X)
        bring_btn.pack(side=LEFT) 
        go_to_news_btn.pack(side=LEFT)
        create_json_btn.pack(side=LEFT)

    def bring_the_news(self):
        headlines_url= "https://newsapi.org/v2/top-headlines"
        api_key="8ab10fb5c558483189eee10bf95cd66d"
        response = requests.get(headlines_url,params={
            "apiKey":api_key,
            "country":"tr",
            "category":"sports",
            "sortBy":"publishedAt",
            "pageSize":50            
        })
        self.sport_news=response.json()["articles"]
        for indeks, news in enumerate(self.sport_news):
            self.lb.insert(indeks, " {} ---> {}".format(news["source"]["name"],news["title"]))
        if len(self.news)>0:
            pass
        else:
            counter=0
            for i in self.sport_news:
                self.news.append({"ID":counter,"Title":i["title"],"Channel":i["source"]["name"],"URL":i["url"]})
                counter+=1
    def go_to_news(self):
        try:
            selected_id=self.lb.curselection()[0]
            for i in self.news:
                if i["ID"]==selected_id:
                    chrome_driver_path="C:\Drivers\chromedriver"
                    driver = webdriver.Chrome(chrome_driver_path)
                    driver.maximize_window()
                    driver.get(i["URL"])
                    time.sleep(50)
        except IndexError:
            messagebox.showerror("Error", "Please first,bring the news!")
    def create_the_json(self):
        if len(self.news)==0:
            messagebox.showerror("Error", "Please first,bring the news!")
        else:
            with open("sport_news.json","w",encoding="utf-8") as file:
                json.dump(self.news,file,ensure_ascii=False,indent=2)
            
root = Tk()
root.title("Turkey Sports News")
app = News(root)
root.mainloop()