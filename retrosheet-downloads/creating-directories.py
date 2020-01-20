# Creating the directories that will hold our downloads

# Now I'm going to add an input to get the right path for different machines

import os
print("The path to where I want to put my retrosheet folder is: /home/tk421/")
retrosheet_home = input("What is the path to where you want to put the retrosheet folder? ")

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
    os.makedirs(regular_events_path) # This one creates retrosheet directory and regular-seaon-events directory inside the retrosheet directory at the same time
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
