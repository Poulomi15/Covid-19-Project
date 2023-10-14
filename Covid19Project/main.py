from plyer import notification
import requests
from bs4 import BeautifulSoup



def notifyMe(title,message):
    notification.notify(
        title = title ,
        message = message, 
        app_icon = "D:\Covid19Project\icon.ico",
        timeout = 10
    )

def getData(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    #notifyMe("Covid-19","Let's get back the healthy world again. ")
    myHTMLData=getData('https://www.mohfw.gov.in/')
    
    soup = BeautifulSoup(myHTMLData, 'html.parser')
    #print(soup.prettify())

for tr in soup.find_all('table')[-1].find_all('tr'):
    print(tr.get_text())

     