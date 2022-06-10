import requests
import json
import plyer
import datetime
import time


while(1):
    # Get covid data by country
    r = requests.get("https://corona-rest-api.herokuapp.com/Api/usa/")
    print(type(r))
    news = r.text
    #print(news)
    dict1 = json.loads(news)
    news_dict = dict1["Success"]
    print(news_dict)

    # Dates/Times
    tod = datetime.date.today()
    todstr = tod.strftime("%d %m %y")

# Generates notifications on PC
    plyer.notification.notify(
        title="Covid-19 Notification"+todstr,
        message="Total cases: "+str(news_dict['cases'])+'\n'
        "Today's cases: "+str(news_dict["todayCases"]) +
        "\nDeaths: "+str(news_dict['deaths']),
        app_icon=r"C:\Users\Administrator\Desktop\icon.ico",
        timeout=3
    )
    time.sleep(7200)