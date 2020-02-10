# Imports
import random

# Raw count numbers
plate_appearances = 186518
home_runs = 6776
triples = 785
doubles = 8531
hits = 42039
singles = hits - home_runs - triples - doubles
walks = 15895
strike_outs = 42823
raw_outs = plate_appearances - hits - walks - strike_outs

# Probabilities
single_probability = singles / plate_appearances
double_probability = doubles / plate_appearances + single_probability
triple_probability = triples / plate_appearances + double_probability
home_run_probability = home_runs / plate_appearances + triple_probability
walk_probability = walks / plate_appearances + home_run_probability
strike_out_probability = strike_outs / plate_appearances + walk_probability
out_probability = raw_outs / plate_appearances + strike_out_probability

# Game variables
outs = 0
hits = 0

# Inning test
while outs < 3:
    play = random.random()
    if play <= single_probability:
        hits += 1
        print("Single")
    elif play <= double_probability:
        hits += 1
        print("Double")
    elif play <= triple_probability:
        hits += 1
        print("Triple")
    elif play <= home_run_probability:
        hits += 1
        print("Home Run")
    elif play <= walk_probability:
        print("Walk")
    elif play <= strike_out_probability:
        outs += 1
        print("Strike Out")
    else:
        outs += 1
        print("Out")
print("Hits %d" % hits)
print("Outs %d" % outs)
