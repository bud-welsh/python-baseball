# The information used here was obtained free of
#      charge from and is copyrighted by Retrosheet.  Interested
#      parties may contact Retrosheet at 20 Sunset Rd.,
#      Newark, DE 19711.

# https://www.retrosheet.org/1900sdis.zip
# /home/tk421/retrosheet/discrepancies

import urllib.request

print("Starting Discrepancy file download")

for year in range(1900, 1980, 10):
    url = 'https://www.retrosheet.org/' + str(year) + 'sdis.zip'
    urllib.request.urlretrieve(url, '/home/tk421/retrosheet/discrepancies/' + str(year) + 'sdis.zip')
    print(str(year) + "'s Discrepancy file downloaded")

print('Download Complete')