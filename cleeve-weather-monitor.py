import os, sys, time
import requests
from lxml import html


SCRAPE_URL = "https://cleeve-weather.grg.org.uk/index.php"


class CleeveWeatherMonitor:


    def getWeather(self):
        page = requests.get(SCRAPE_URL)
        tree = html.fromstring(page.content)
        print(page)
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