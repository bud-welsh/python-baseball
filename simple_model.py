# Imports
import random

# Raw count numbers
plate_appearances = 186518
home_runs = 6776
triples = 785
doubles = 8531
raw_hits = 42039
singles = raw_hits - home_runs - triples - doubles
walks = 15895
strike_outs = 42823
raw_outs = plate_appearances - raw_hits - walks - strike_outs

# Probabilities
single_probability = singles / plate_appearances
double_probability = doubles / plate_appearances + single_probability
triple_probability = triples / plate_appearances + double_probability
home_run_probability = home_runs / plate_appearances + triple_probability
walk_probability = walks / plate_appearances + home_run_probability
strike_out_probability = strike_outs / plate_appearances + walk_probability
out_probability = raw_outs / plate_appearances + strike_out_probability

# Game variables
top_of_inning = True
inning = 1
outs = 0
home_team_hits = 0
away_team_hits = 0
home_team_runs = 0
away_team_runs = 0
home_team_left_on_base = 0
away_team_left_on_base = 0
inning_runs = 0
inning_hits = 0
inning_left_on_base = 0
first_runner = False
second_runner = False
third_runner = False
end_of_game = False

# Inning test
while end_of_game == False:
    if top_of_inning == True:
        print("Here's the top of inning number %s." % inning)
    else:
        print("Here's the bottom of inning number %s." % inning)
    while outs < 3:
        play = random.random()
        if play <= single_probability:
            inning_hits += 1
            if top_of_inning == False:
                home_team_hits += 1
            else:
                away_team_hits += 1
            print("Batter hits a single.")
            if third_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                third_runner = False
                print("Runner on third scores.")
            else:
                pass
            if second_runner == True:
                second_runner = False
                third_runner = True
                print("Runner on second advances to third.")
            else:
                pass
            if first_runner == True:
                first_runner = False
                second_runner = True
                print("Runner on first advances to second.")
            else:
                pass
            first_runner = True
        elif play <= double_probability:
            inning_hits += 1
            if top_of_inning == False:
                home_team_hits += 1
            else:
                away_team_hits += 1
            print("Batter hits a double.")
            if third_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                print("Runner on third scores.")
                third_runner = False
            else:
                pass
            if second_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                print("Runner on second scores.")
                second_runner = False
            else:
                pass
            if first_runner == True:
                third_runner = True
                print("Runner on first goes to third.")
                first_runner = False
            else:
                pass
            second_runner = True
        elif play <= triple_probability:
            inning_hits += 1
            if top_of_inning == False:
                home_team_hits += 1
            else:
                away_team_hits += 1
            print("The batter hits a triple.")
            if third_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                print("Runner on third scores.")
                third_runner = False
            else:
                pass
            if second_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                print("Runner on second scores.")
                second_runner = False
            else:
                pass
            if first_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                print("Runner on first scores.")
                first_runner = False
            else:
                pass
            third_runner = True
        elif play <= home_run_probability:
            inning_hits += 1
            if top_of_inning == False:
                home_team_hits += 1
            else:
                away_team_hits += 1
            inning_runs += 1
            if top_of_inning == False:
                home_team_runs += 1
            else:
                away_team_runs += 1
            print("There's a home run.")
            if third_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                print("Runner on third scores.")
                third_runner = False
            else:
                pass
            if second_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                print("Runner on second scores.")
                second_runner = False
            else:
                pass
            if first_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                print("Runner on first scores.")
                first_runner = False
            else:
                pass
        elif play <= walk_probability:
            print("Batter takes a walk.")
            if third_runner == True and second_runner == True and first_runner == True:
                inning_runs += 1
                if top_of_inning == False:
                    home_team_runs += 1
                else:
                    away_team_runs += 1
                print("Runner on third walks home, and bases are still loaded.")
            else:
                pass
            if third_runner == False and second_runner == True and first_runner == True:
                third_runner = True
                print("After the walk, the bases are now loaded.")
            else:
                pass
            if third_runner == False and second_runner == False and first_runner == True:
                second_runner = True
                print("Runners are on first and second.")
            else:
                pass
            if third_runner == False and second_runner == False and first_runner == False:
                first_runner = True
            else:
                pass
        elif play <= strike_out_probability:
            outs += 1
            print("Batter strikes out.")
        else:
            outs += 1
            print("Batter is out.")
        if inning >= 9 and top_of_inning == False and home_team_runs > away_team_runs:
            print("With %s outs in the inning the home team just got a walk off win." % outs)
            outs = 3
            end_of_game = True
        else:
            pass
    if first_runner == True:
        inning_left_on_base += 1
        if top_of_inning == False:
            home_team_left_on_base += 1
        else:
            away_team_left_on_base += 1
    else:
        pass
    if second_runner == True:
        inning_left_on_base += 1
        if top_of_inning == False:
            home_team_left_on_base += 1
        else:
            away_team_left_on_base += 1
    else:
        pass
    if third_runner == True:
        inning_left_on_base += 1
        if top_of_inning == False:
            home_team_left_on_base += 1
        else:
            away_team_left_on_base += 1
    else:
        pass
    print("At the end of this half inning, %s runs on %s hits and %s left on base." %(inning_runs, inning_hits, inning_left_on_base))
    outs = 0
    inning_runs = 0
    inning_hits = 0
    inning_left_on_base = 0
    first_runner = False
    second_runner = False
    third_runner = False
    if inning == 9 and top_of_inning == True and home_team_runs > away_team_runs:
        end_of_game = True
    elif inning >= 9 and top_of_inning == False and home_team_runs < away_team_runs:
        end_of_game = True
    else:
        if top_of_inning == True:
            top_of_inning = False
        else:
            inning += 1
            top_of_inning = True
print("Today's game totals are for the visiting team, %s runs on %s hits while leving %s runners on base." % (away_team_runs, away_team_hits, away_team_left_on_base))
print("And for the home team, %s runs on %s hits, and left %s runners on base." % (home_team_runs, home_team_hits, home_team_left_on_base))    