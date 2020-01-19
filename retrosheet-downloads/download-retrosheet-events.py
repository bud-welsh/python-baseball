# This will download all the event files from 1918 to 2019 from retrosheet.org.

# The information used here was obtained free of
#      charge from and is copyrighted by Retrosheet.  Interested
#      parties may contact Retrosheet at 20 Sunset Rd.,
#      Newark, DE 19711.

# https://www.retrosheet.org/game.htm has the event file links.

# These are the paths to the yearly event files on retrosheet.org:
# https://www.retrosheet.org/events/1918eve.zip
# https://www.retrosheet.org/events/1919eve.zip

# Found urllib.request module from an article, https://stackabuse.com/download-files-with-python/, and the python documents, https://docs.python.org/3/library/urllib.request.html#module-urllib.request.

import urllib.request 

print("Starting to download event files")

for year in range(1918, 2020):
    url = "https://www.retrosheet.org/events/" + str(year) + "eve.zip"
    urllib.request.urlretrieve(url, '/home/tk421/retrosheet/regular-season-events/' + str(year) + 'eve.zip')
    print("Downloading " + str(year) + " event files")

print("Event files download complete")
