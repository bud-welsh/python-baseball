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
doubles_probability = doubles / plate_appearances
triple_probability = triples / plate_appearances
home_run_probability = home_runs / plate_appearances
walk_probability = walks / plate_appearances
strike_out_probability = strike_outs / plate_appearances
out_probability = raw_outs / plate_appearances

# Game variables
outs = 0
hits = 0

