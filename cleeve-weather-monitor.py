import os, sys, time
import requests
from bs4 import BeautifulSoup


SCRAPE_URL = "https://cleeve-weather.grg.org.uk"


class CleeveWeatherMonitor:


    def getWeather(self):

        # Get weather table from page. Note, there is no
        # id for the table, so it needs to be grabbed using the
        # width property. Not nice, but it works.

        count = 0

        # Find and get the weather table
        page = requests.get(SCRAPE_URL).text
        soup = BeautifulSoup(page, "lxml")
        weather_table = soup.find('table', attrs={'width':'40%'})

        # Get the table rows we care about
        rows = weather_table.find_all('tr')

        row_time = rows[1]
        row_current_pressure = rows[5]
        row_current_wind = rows[9]
        row_rain_today = rows[13]
        row_rain_recent = rows[14]
        row_temp_current = rows[18]
        row_temp_windchill = rows[19]
        row_temp_today_max = rows[20]
        row_temp_today_min= rows[21] 

        # Get the row content that we want

        # TIME
        soup = BeautifulSoup(str(row_time), 'html.parser')
        td = soup.find_all('td')
        time = td[0].text

        #PRESSURE
        soup = BeautifulSoup(str(row_current_pressure), 'html.parser')
        td = soup.find_all('td')
        current_pressure = td[0].text

        #WIND
        soup = BeautifulSoup(str(row_current_wind), 'html.parser')
        td = soup.find_all('td')
        current_wind = td[0].text

        # RAIN TODAY

            # TODO

        # RAIN RECENTLY

            # TODO

        # TEMP

            # TODO

        # WINDCHILL

            # TODO

        # TEMP MAX TODAY

            # TODO

        # TEMP MIN TODAY

            # TODO

        # Print all the things
        print("TIME: %s" % time)
        print("PRESSURE: %s" % current_pressure)
        print("WIND: %s" % current_wind)
        #print("RAIN TODAY: %s" % rain_today)
        #print("RAIN_RECENTLY: %s" % rain_recent)
        #print("TEMP: %s" % temp_current)
        #print("WINDCHILL: %s" % temp_windchill)
        #print("TEMP MAX: %s" % temp_today_max)
        #print("TEMP MIN: %s" % temp_today_min)

        #
        # We dont need this any more, for row debugging
        #

#       for row in rows:
#           print("%d: %s" % (count, row) )
#           count = count +1
#           rowtext = str(row)
#           if rowtext.startswith('<tr>'):
#           print(row)
    
        return


    def watch(self, interval=10):
        print("\n => Watching weather every %s seconds\n" % interval)

        try:
            while True:
                
                weather = self.getWeather()
                time.sleep(10)

        except KeyboardInterrupt:
            print('interrupted!')
            print("")

weatherMonitor = CleeveWeatherMonitor()
weatherMonitor.watch()