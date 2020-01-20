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
disrepancy_path = retrosheet_home + 'retrosheet/discrepancy-files'
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
    os.mkdir(disrepancy_path)
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
    print("Creation of directory %s failed" % disrepancy_path)
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
    print("Successful creation of directory %s" % disrepancy_path)
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

# Extract all of zip files.
print("Beginning the extracting process now.")

# Extract all of the regular season event files.
print("Extracting all of the regular season event files.")

for year in range(1910, 2020, 10):
    with ZipFile(zip_file_path + '/' + str(year) + 'seve.zip', 'r') as regular_event_files:
        regular_event_files.extractall(regular_events_path)
        print("Extracted %s's event files." % year)

print("Extracted all of the regular season event files.")