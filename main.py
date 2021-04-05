from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def NotifyMe(title, message):
    notification.notify(
        title = title, 
        message = message, 
        app_icon = None,
        # app_icon = "C:\Users\Shivam-Bam\Desktop\Projects with Python\COVID-19 R_T Notification Sys\icon.ico", 
        timeout = 5
    )

def getdata(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    # NotifyMe("COVID-19", "help to stop spreading of corona virus")
    MyHtmlData = getdata('https://www.mohfw.gov.in/')
    # print(MyHtmlData)

    soup = BeautifulSoup(MyHtmlData, "html.parser")
    # print(soup.prettify())
    # mystrData = ""

    # for tr in soup.find_all('tbody')[15].find_all('tr'):
    #     print(tr)


    for tr in soup.find_all('tbody')[1]:
        tds = tr.find_all('tr')
        print(tds.text)



    # for tr in soup.find_all('tbody')[1].find_all('tr'):
    #     mystrData += tr.get_text()
    # mystrData = mystrData[1:]
    # itemlist = mystrData.split("\n\n")

    # states = ['Delhi', 'chandigarh']

    # for item in itemlist[0:22]:
    #     DataList = item.split("\n")
    #     if DataList[1] in states:
    #         print(DataList)
    #         nTitle = 'cases of covid-19'
    #         nText = f"{DataList[1]} Indian:{DataList[2]} Foreign:{DataList[3]} Cured:{DataList[4]} Death:{DataList[5]}"
    #         print(nTitle, nText)
    #         time.sleep(3)
