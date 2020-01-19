# https://www.retrosheet.org/events/allpost.zip

# The information used here was obtained free of
#      charge from and is copyrighted by Retrosheet.  Interested
#      parties may contact Retrosheet at 20 Sunset Rd.,
#      Newark, DE 19711.

import urllib.request

print("Starting Post-Season Event files download.")

url = 'https://www.retrosheet.org/events/allpost.zip'
urllib.request.urlretrieve(url, '/home/tk421/retrosheet/post-season-events/allpost.zip')

print("Download Complete")
