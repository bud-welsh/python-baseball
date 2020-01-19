# This will download all the box score files from 1904 to 1973 from retrosheet.org.
# 1960 and 1961 are missing from individual years and the decade files so we will download by decade instead of individual years because the individual years breaks at 1960 and 1961.

# The information used here was obtained free of
#      charge from and is copyrighted by Retrosheet.  Interested
#      parties may contact Retrosheet at 20 Sunset Rd.,
#      Newark, DE 19711.

# https://www.retrosheet.org/game.htm has the event file links.

# These are the paths to the yearly box score files on retrosheet.org:
# https://www.retrosheet.org/events/1900sbox.zip
# https://www.retrosheet.org/events/1910sbox.zip

# Found urllib.request module from an article, https://stackabuse.com/download-files-with-python/, and the python documents, https://docs.python.org/3/library/urllib.request.html#module-urllib.request.

import urllib.request 

year_download = 1900 # This is the earliest year that retrosheet has available for regular season box score files.

print("Starting to download box score files.")

while year_download < 1960:
    url = "https://www.retrosheet.org/events/" + str(year_download) + "sbox.zip"
    urllib.request.urlretrieve(url, '/home/tk421/retrosheet/regular-season-box-scores/' + str(year_download) + 'sbox.zip')
    print("Downloading " + str(year_download) + "'s box score files") # I don't need this step, but it is nice to see it anyway because of the amount of time it takes to download each file.
    year_download += 10

print("Box score files download complete.")

