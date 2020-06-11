import pandas as pd
import urllib
from bs4 import BeautifulSoup

class getTable():
    def __init__ (self, url):
        res=urllib.request.urlopen(url)
        html=res.read()
        self.soup = BeautifulSoup(html, "html.parser")
        
    def check_order(self):
        h2 = self.soup.find_all("h2")
        key = [i.string for i in h2]
        return [i for i in key if i != None]

    def maketable(self):
        gdp_table = self.soup.find_all("table", attrs={"class": "data"})
        
        results = []
        for table in gdp_table:
            df = pd.read_html(str(table))           
            results.append(df)

        return results
