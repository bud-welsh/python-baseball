# This will download all the event files from 1918 to 2019 from retrosheet.org
# 19 January 2020

# https://www.retrosheet.org/events/1918eve.zip
# https://www.retrosheet.org/events/1919eve.zip

import urllib.request 

year_download = 1918

print("Starting to download event files")

while year_download < 2020:
    url = "https://www.retrosheet.org/events/" + str(year_download) + "eve.zip"
    urllib.request.urlretrieve(url, '/home/tk421/retrosheet/regular-season-events/' + str(year_download) + 'eve.zip')
    print("Downloading " + str(year_download) + " event files") # Don't need this step, but I want to see it anyway"
    year_download += 1

print("Event files download complete")
