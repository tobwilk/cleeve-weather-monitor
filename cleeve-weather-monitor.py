import os, sys, time
import requests
from bs4 import BeautifulSoup


SCRAPE_URL = "https://cleeve-weather.grg.org.uk"


class CleeveWeatherMonitor:

    def getWeather_APRS_API(self):

        #
        # TODO, use the APRS.fi API to pull the data, rather than scraping
        # the web page. https://aprs.fi/page/api
        #

        return(0)

        

    def getWeather_webscrapper(self):

        # Get weather table from page. Note, there is no
        # id for the table, so it needs to be grabbed using the
        # width property. Not nice, but it works.

        # count = 0 used for debug

        json_data = {}

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
        json_data['time'] = time

        #PRESSURE
        soup = BeautifulSoup(str(row_current_pressure), 'html.parser')
        td = soup.find_all('td')
        current_pressure = td[0].text
        json_data['current_pressure'] = current_pressure

        #WIND
        soup = BeautifulSoup(str(row_current_wind), 'html.parser')
        td = soup.find_all('td')
        current_wind = td[0].text
        json_data['current_wind'] = current_wind

        # RAIN TODAY

        soup = BeautifulSoup(str(row_rain_today), 'html.parser')
        td = soup.find_all('td')
        rain_today = td[0].text
        json_data['rain_today'] = rain_today

        # RAIN RECENTLY

        soup = BeautifulSoup(str(row_rain_recent), 'html.parser')
        td = soup.find_all('td')
        rain_recent = td[0].text
        json_data['rain_recent'] = rain_recent

        # TEMP

        soup = BeautifulSoup(str(row_temp_current), 'html.parser')
        td = soup.find_all('td')
        temp_current = td[1].text
        json_data['temp_current'] = temp_current

        # WINDCHILL

        soup = BeautifulSoup(str(row_temp_windchill), 'html.parser')
        td = soup.find_all('td')
        temp_windchill = td[1].text
        json_data['temp_windchill'] = temp_windchill

        # TEMP MAX TODAY

        soup = BeautifulSoup(str(row_temp_today_max), 'html.parser')
        td = soup.find_all('td')
        temp_today_max = td[1].text
        json_data['temp_today_max'] = temp_today_max

        # TEMP MIN TODAY

        soup = BeautifulSoup(str(row_temp_today_min), 'html.parser')
        td = soup.find_all('td')
        temp_today_min = td[1].text
        json_data['temp_today_min'] = temp_today_min

        return(json_data)

        #
        # debug code
        #

        #       for row in rows:
        #           print("%d: %s" % (count, row) )
        #           count = count +1
        #           rowtext = str(row)
        #           if rowtext.startswith('<tr>'):
        #           print(row)


    def watch(self, interval=10):
        print("\n => Watching weather every %s seconds\n" % interval)

        try:
            while True:
                
                weather = self.webscrapper()
                
                # Print all the things
                print("\n\nTIME: %s" % weather['time'])
                print("PRESSURE: %s" % weather['current_pressure'])
                print("WIND: %s" % weather['current_wind'])
                print("RAIN TODAY: %s" % weather['rain_today'])
                print("RAIN_RECENTLY: %s" % weather['rain_recent'])
                print("TEMP: %s" % weather['temp_current'])
                print("WINDCHILL: %s" % weather['temp_windchill'])
                print("TEMP MAX: %s" % weather['temp_today_max'])
                print("TEMP MIN: %s" % weather['temp_today_min'])

                time.sleep(10)

        except KeyboardInterrupt:
            print('interrupted!')
            print("")


weatherMonitor = CleeveWeatherMonitor()
weatherMonitor.watch()