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

regular_events_path = retrosheet_home + 'retrosheet/regular-season-events/zip-files' 
regular_box_path = retrosheet_home + 'retrosheet/regular-box-score/zip-files'
allstar_events_path = retrosheet_home + 'retrosheet/all-star-events/zip-files'
postseason_events_path = retrosheet_home + 'retrosheet/post-season-events/zip-files'
disrepancy_path = retrosheet_home + 'retrosheet/discrepancy-files'
regular_gamelog_path = retrosheet_home + 'retrosheet/regular-season-game-logs/zip-files'
world_series_gamelog_path = retrosheet_home + 'retrosheet/world-series-game-logs/zip-files'
allstar_gamelog_path = retrosheet_home + 'retrosheet/all-star-game-logs/zip-files'
wildcard_gamelog_path = retrosheet_home + 'retrosheet/wild-card-game-logs/zip-files'
lds_gamelog_path = retrosheet_home + 'retrosheet/league-divisional-series-game-logs/zip-files'
lcs_gamelog_path = retrosheet_home + 'retrosheet/league-championship-series-game-logs/zip-files'
regular_schedule_path = retrosheet_home + 'retrosheet/regular-season-schedules/zip-files'

try:
    os.makedirs(regular_events_path) 
    os.makedirs(regular_box_path)
    os.makedirs(allstar_events_path)
    os.makedirs(postseason_events_path)
    os.makedirs(disrepancy_path)
    os.makedirs(regular_gamelog_path)
    os.makedirs(world_series_gamelog_path)
    os.makedirs(allstar_gamelog_path)
    os.makedirs(wildcard_gamelog_path)
    os.makedirs(lds_gamelog_path)
    os.makedirs(lcs_gamelog_path)
    os.makedirs(regular_schedule_path)
except OSError:
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

# Download all of the regular season event files.
print("Starting to download all of the regular season event files from 1918 to 2019")

for year in range(1910, 2020, 10):
    url = 'https://www.retrosheet.org/events/' + str(year) + 'seve.zip'
    urllib.request.urlretrieve(url, regular_events_path + '/' + str(year) + 'seve.zip')
    print("%ss regular season event files is now downloaded." % year)

print("The regular season event files download is complete.")

# Extract all of zip files.

# Extract all of the regular season event.
