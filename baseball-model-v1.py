# Here are the batting variables.
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
sacrifice_hits = 776
sacrifice_flies = 1150



# The first half inning
for outs in range(0, 4):
    if outs < 3:
        print("Batter up!")
        print("Batter strikes out.")
        outs += 1
    else:
        print("That's the end of the half inning.")