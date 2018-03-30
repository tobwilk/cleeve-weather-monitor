import os, sys, time
import requests
from bs4 import BeautifulSoup


SCRAPE_URL = "https://cleeve-weather.grg.org.uk"


class CleeveWeatherMonitor:


    def getWeather(self):

        # Get weather table from page. Note, there is no
        # id for the table, so it needs to be grabbed using the
        # width property. Not nice, but it works.

        page = requests.get(SCRAPE_URL).text
        soup = BeautifulSoup(page, "lxml")
        table = soup.find('table', attrs={'width':'40%'})

        data = []

        # parse rows
        rows = table.find_all('tr')
        for row in rows:
            #print(row)
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty values

            print(data)
        
        return("null")


    def watch(self, interval=10):
        print("\n => Watching weather every %s seconds\n" % interval)

        try:
            while True:
                
                weather = self.getWeather()
                print( weather )

                time.sleep(10)
        except KeyboardInterrupt:
            print('interrupted!')
            print("")

weatherMonitor = CleeveWeatherMonitor()
weatherMonitor.watch()