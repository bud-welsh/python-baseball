# There is not a file for the 1945 All-Star Game because it was cancelled. We will do this with 2 for loops.

# The information used here was obtained free of
#      charge from and is copyrighted by Retrosheet.  Interested
#      parties may contact Retrosheet at 20 Sunset Rd.,
#      Newark, DE 19711.

# https://www.retrosheet.org/events/1933as.zip

import urllib.request

for year in range(1933, 1945):
    url = 'https://www.retrosheet.org/events/' + str(year) + 'as.zip'
    urllib.request.urlretrieve(url, '/home/tk421/retrosheet/allstar-events/' + str(year) + 'as.zip')
    print(str(year) + "All-Star Event files are downloaded.")

for year in range(1946, 2020):
    url = 'https://www.retrosheet.org/events/' + str(year) + 'as.zip'
    urllib.request.urlretrieve(url, '/home/tk421/retrosheet/allstar-events/' + str(year) + 'as.zip')
    print(str(year) + " All-Star Event files are downloaded.")

print("Downloads Complete")