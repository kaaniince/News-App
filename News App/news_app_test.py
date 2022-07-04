from tkinter import *
from news_app import News

def main():
        
    root = Tk()
    root.title("Turkey Sports News")
    app = News(root)
    root.mainloop()

main()