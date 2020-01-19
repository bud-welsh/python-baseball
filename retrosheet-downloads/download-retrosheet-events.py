# This will download all the event files from 1918 to 2019 from retrosheet.org.

# https://www.retrosheet.org/game.htm has the event file links.

# These are the paths to the yearly event files on retrosheet.org:
# https://www.retrosheet.org/events/1918eve.zip
# https://www.retrosheet.org/events/1919eve.zip

# Found urllib.request module from an article, https://stackabuse.com/download-files-with-python/, and the python documents, https://docs.python.org/3/library/urllib.request.html#module-urllib.request.

import urllib.request 

year_download = 1918 # This is the earliest year that retrosheet has available for regular season event files.

print("Starting to download event files")

while year_download < 2020:
    url = "https://www.retrosheet.org/events/" + str(year_download) + "eve.zip"
    urllib.request.urlretrieve(url, '/home/tk421/retrosheet/regular-season-events/' + str(year_download) + 'eve.zip')
    print("Downloading " + str(year_download) + " event files") # I don't need this step, but it is nice to see it anyway because of the amount of time it takes to download each file.
    year_download += 1

print("Event files download complete")
