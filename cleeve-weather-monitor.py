import os, sys, time


class CleeveWeatherMonitor:
    variable = "blah"

    def getWeather(self):
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