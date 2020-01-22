# Here are the 2019 batting variables.
plate_apperances = 186518
at_bats = 166651
hits = 42039
doubles = 8531
triples = 785
home_runs = 6776
singles = (42039 - doubles - triples - home_runs)
walks = 15895
strike_outs = 42823
hit_by_pitch = 1984
outs = (plate_apperances - hits - walks - hit_by_pitch - strike_outs)

# These are the 2019 random batting percentages
single_average = singles / plate_apperances
double_average = doubles / plate_apperances
triple_average = triples / plate_apperances
home_run_average = home_runs / plate_apperances
walk_average = walks / plate_apperances
strike_out_average = strike_outs / plate_apperances
hit_by_pitch_average = hit_by_pitch / plate_apperances
out_average = outs / plate_apperances

print(single_average + double_average + triple_average + home_run_average + walk_average + strike_out_average + hit_by_pitch_average + out_average)

# The first half inning
for outs in range(0, 4):
    if outs < 3:
        print("Batter up!")
        print("Batter strikes out.")
        outs += 1
    else:
        print("That's the end of the half inning.")