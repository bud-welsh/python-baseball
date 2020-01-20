# Recipients of Retrosheet data are free to make any desired use of
# the information, including (but not limited to) selling it,
# giving it away, or producing a commercial product based upon the
# data.  Retrosheet has one requirement for any such transfer of
# data or product development, which is that the following
# statement must appear prominently:

#      The information used here was obtained free of
#      charge from and is copyrighted by Retrosheet.  Interested
#      parties may contact Retrosheet at "www.retrosheet.org".

# Retrosheet makes no guarantees of accuracy for the information 
# that is supplied. Much effort is expended to make our website 
# as correct as possible, but Retrosheet shall not be held 
# responsible for any consequences arising from the use the 
# material presented here. All information is subject to corrections 
# as additional data are received. We are grateful to anyone who
# discovers discrepancies and we appreciate learning of the details. 

# This will download all the retrosheet files into directories that this will create, and it will extract all of the zip files too. 

# Import modules.
import os
import urllib.request
from zipfile import ZipFile

# Create directories to store the retrosheet zip files.
print("The path to where I want to put my retrosheet folder is: /home/tk421/.")
retrosheet_home = input("What is the path to where you want to put the retrosheet folder? ")

zip_file_path = retrosheet_home + 'retrosheet/zip-files'
regular_events_path = retrosheet_home + 'retrosheet/regular-season-events' 
regular_box_path = retrosheet_home + 'retrosheet/regular-box-score'
allstar_events_path = retrosheet_home + 'retrosheet/all-star-events'
postseason_events_path = retrosheet_home + 'retrosheet/post-season-events'
discrepancy_path = retrosheet_home + 'retrosheet/discrepancy-files'
regular_gamelog_path = retrosheet_home + 'retrosheet/regular-season-game-logs'
world_series_gamelog_path = retrosheet_home + 'retrosheet/world-series-game-logs'
allstar_gamelog_path = retrosheet_home + 'retrosheet/all-star-game-logs'
wildcard_gamelog_path = retrosheet_home + 'retrosheet/wild-card-game-logs'
lds_gamelog_path = retrosheet_home + 'retrosheet/league-divisional-series-game-logs'
lcs_gamelog_path = retrosheet_home + 'retrosheet/league-championship-series-game-logs'
regular_schedule_path = retrosheet_home + 'retrosheet/regular-season-schedules'

try:
    os.makedirs(zip_file_path)
    os.mkdir(regular_events_path) 
    os.mkdir(regular_box_path)
    os.mkdir(allstar_events_path)
    os.mkdir(postseason_events_path)
    os.mkdir(discrepancy_path)
    os.mkdir(regular_gamelog_path)
    os.mkdir(world_series_gamelog_path)
    os.mkdir(allstar_gamelog_path)
    os.mkdir(wildcard_gamelog_path)
    os.mkdir(lds_gamelog_path)
    os.mkdir(lcs_gamelog_path)
    os.mkdir(regular_schedule_path)
except OSError:
    print("Creation of directory %s failed" % zip_file_path)
    print("Creation of directory %s failed" % regular_events_path)
    print("Creation of directory %s failed" % regular_box_path)
    print("Creation of directory %s failed" % allstar_events_path)
    print("Creation of directory %s failed" % postseason_events_path)
    print("Creation of directory %s failed" % discrepancy_path)
    print("Creation of directory %s failed" % regular_gamelog_path)
    print("Creation of directory %s failed" % world_series_gamelog_path)
    print("Creation of directory %s failed" % allstar_gamelog_path)
    print("Creation of directory %s failed" % wildcard_gamelog_path)
    print("Creation of directory %s failed" % lds_gamelog_path)
    print("Creation of directory %s failed" % lcs_gamelog_path)
    print("Creation of directory %s failed" % regular_schedule_path)
else:
    print("Successful creation of directory %s" % zip_file_path)
    print("Successful creation of directory %s" % regular_events_path)
    print("Successful creation of directory %s" % regular_box_path)
    print("Successful creation of directory %s" % allstar_events_path)
    print("Successful creation of directory %s" % postseason_events_path)
    print("Successful creation of directory %s" % discrepancy_path)
    print("Successful creation of directory %s" % regular_gamelog_path)
    print("Successful creation of directory %s" % world_series_gamelog_path)
    print("Successful creation of directory %s" % allstar_gamelog_path)
    print("Successful creation of directory %s" % wildcard_gamelog_path)
    print("Successful creation of directory %s" % lds_gamelog_path)
    print("Successful creation of directory %s" % lcs_gamelog_path)
    print("Successful creation of directory %s" % regular_schedule_path)

print("All directories are created.")

# Download all of the files.
print("Beginning the download process now.")

# Download all of the regular season event files.
print("Starting to download all of the regular season event files from 1918 to 2019.")

for year in range(1910, 2020, 10):
    url = 'https://www.retrosheet.org/events/' + str(year) + 'seve.zip'
    urllib.request.urlretrieve(url, zip_file_path + '/' + str(year) + 'seve.zip')
    print("%ss regular season event files is now downloaded." % year)

print("The regular season event files download is complete.")

# Download all of the regular season box score files.
print("Starting to download all of the regular season box score files from 1871, 1872, and 1874.")

# Download 1871, 1872, and 1874 box score files.
url = 'https://www.retrosheet.org/events/1871box.zip'
urllib.request.urlretrieve(url, zip_file_path + '/1871box.zip')
print("1871 regular season box score file is now downloaded")

url = 'https://www.retrosheet.org/events/1872box.zip'
urllib.request.urlretrieve(url, zip_file_path + '/1872box.zip')
print("1872 regular season box score file is now downloaded")

url = 'https://www.retrosheet.org/events/1874box.zip'
urllib.request.urlretrieve(url, zip_file_path + '/1874box.zip')
print("1874 regular season box score file is now downloaded")

print("Beginning to download all of the regular season box score files from 1904 to 1973 except 1960 and 1961 are missing.")
for year in range(1900 , 1960, 10):
    url = 'https://www.retrosheet.org/events/' + str(year) + 'sbox.zip'
    urllib.request.urlretrieve(url, zip_file_path + '/' + str(year) + 'box.zip')
    print("%s's regular season box score files is now downloaded." % year)
print('The regular season box score files are now downloaded.')

# Download all All-Star Game event files.
url = 'https://www.retrosheet.org/events/allas.zip'
urllib.request.urlretrieve(url, zip_file_path + '/allas.zip')
print("All All-Star Game event files are now downloaded")

# Download all Post-Season event files.
url = 'https://www.retrosheet.org/events/allpost.zip'
urllib.request.urlretrieve(url, zip_file_path + '/allpost.zip')
print("All All-Star Game event files are now downloaded")

#Download all Discrepancy files 
print("Beginning to download all of the Discrepancy files from 1909 to 1975.")
for year in range(1900 , 1980, 10):
    url = 'https://www.retrosheet.org/' + str(year) + 'sdis.zip'
    urllib.request.urlretrieve(url, zip_file_path + '/' + str(year) + 'sdis.zip')
    print("%s's discrepancy files is now downloaded." % year)
print('The discrepancy files are now downloaded.')

# Download all regular season game log files
print("Beginning to download all of the regular season game log files from 1871 to 2019.")
url = 'https://www.retrosheet.org/gamelogs/gl1871_2019.zip'
urllib.request.urlretrieve(url, zip_file_path + '/gl1871_2019.zip')
print('All regular season game log files are now downloaded.')

# Download all World Series game log files
print("Beginning to download all of the World Series game log files.")
url = 'https://www.retrosheet.org/gamelogs/glws.zip'
urllib.request.urlretrieve(url, zip_file_path + '/glws.zip')
print('All World Series game log files are now downloaded.')

# Download all All-Star game log files
print("Beginning to download all of the World Series game log files.")
url = 'https://www.retrosheet.org/gamelogs/glas.zip'
urllib.request.urlretrieve(url, zip_file_path + '/glas.zip')
print('All All-Star game log files are now downloaded.')

# Download all Wild Card game log files
print("Beginning to download all of the World Series game log files.")
url = 'https://www.retrosheet.org/gamelogs/glwc.zip'
urllib.request.urlretrieve(url, zip_file_path + '/glwc.zip')
print('All Wild Card game log files are now downloaded.')

# Download all League Divisional Series game log files
print("Beginning to download all of the World Series game log files.")
url = 'https://www.retrosheet.org/gamelogs/gldv.zip'
urllib.request.urlretrieve(url, zip_file_path + '/gldv.zip')
print('All League Divisional Series game log files are now downloaded.')

# Download all League Championship Series game log files
print("Beginning to download all of the World Series game log files.")
url = 'https://www.retrosheet.org/gamelogs/gllc.zip'
urllib.request.urlretrieve(url, zip_file_path + '/gllc.zip')
print('All League Championship Series game log files are now downloaded.')

# Extract all of zip files.
print("Beginning the extracting process now.")

# Extract all of the regular season event files.
print("Extracting all of the regular season event files.")

for year in range(1910, 2020, 10):
    with ZipFile(zip_file_path + '/' + str(year) + 'seve.zip', 'r') as regular_event_files:
        regular_event_files.extractall(regular_events_path)
        print("Extracted %s's event files." % year)

print("Extracted all of the regular season event files.")

# Extrat all of the regular season box score files.
print("Extracting all of the regular season box score files.")

with ZipFile(zip_file_path + '/1871box.zip', 'r') as regular_box_files:
    regular_box_files.extractall(regular_box_path)
    print("Extracted 1871 regular season box score files.")

with ZipFile(zip_file_path + '/1872box.zip', 'r') as regular_box_files:
    regular_box_files.extractall(regular_box_path)
    print("Extracted 1872 reagular season box score files.")

with ZipFile(zip_file_path + '/1874box.zip', 'r') as regular_box_files:
    regular_box_files.extractall(regular_box_path)
    print("Extracted 1874 regular season box score files.")

for year in range(1900, 1960, 10):
    with ZipFile(zip_file_path + '/' + str(year) + 'box.zip', 'r') as regular_box_files:
        regular_box_files.extractall(regular_box_path)
        print("Extracted %s's regular season box score files." % year)

print("Extracted all of the regular season box score files.")

# Extract all All-Star Game event files.
with ZipFile(zip_file_path + '/allas.zip', 'r') as allstar_events_files:
    allstar_events_files.extractall(allstar_events_path)
    print("Extracted all All-Star Game event files except for 1945 when there was no All-Star Game.")

# Extract all Post-Season event files.
with ZipFile(zip_file_path + '/allpost.zip', 'r') as postseason_events_file:
    postseason_events_file.extractall(postseason_events_path)
    print("Extracted all Post-Season event files except for 1904 and 1994 when there was not any post-seasons.")

# Extract all Discrepancy files.
for year in range(1900, 1980, 10):
    with ZipFile(zip_file_path + '/' + str(year) + 'sdis.zip', 'r') as discrepancy_files:
        discrepancy_files.extractall(discrepancy_path)
        print("Extracted %s's discrepancy files." % year)

print("Extracted all of the discrepancy files.")

# Extract all regular season game log files.
with ZipFile(zip_file_path + '/gl1871_2019.zip', 'r') as regular_gamelog_files:
    regular_gamelog_files.extractall(regular_gamelog_path)
    print("Extracted all regular season game log files.")

# Extract all World Series game log files.
with ZipFile(zip_file_path + '/glws.zip', 'r') as world_series_gamelog_files:
    world_series_gamelog_files.extractall(world_series_gamelog_path)
    print("Extracted all World Series game log files.")
    
# Extract all All-Star game log files.
with ZipFile(zip_file_path + '/glas.zip', 'r') as allstar_gamelog_files:
    allstar_gamelog_files.extractall(allstar_gamelog_path)
    print("Extracted all All-Star game log files.")

# Extract all Wild Card game log files.
with ZipFile(zip_file_path + '/glwc.zip', 'r') as wildcard_gamelog_files:
    wildcard_gamelog_files.extractall(wildcard_gamelog_path)
    print("Extracted all Wild Card game log files.")

# Extract all League Divisional Series game log files.
with ZipFile(zip_file_path + '/gldv.zip', 'r') as lds_gamelog_files:
    lds_gamelog_files.extractall(lds_gamelog_path)
    print("Extracted all League Divisional Series game log files.")

# Extract all League Championship Series game log files.
with ZipFile(zip_file_path + '/gllc.zip', 'r') as lcs_gamelog_files:
    lcs_gamelog_files.extractall(lcs_gamelog_path)
    print("Extracted all League Championship Series game log files.")