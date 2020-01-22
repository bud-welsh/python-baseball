

# Here are the 2019 batting variables.
plate_apperances_raw = 186518
at_bats_raw = 166651
hits_raw = 42039
doubles_raw = 8531
triples_raw = 785
home_runs_raw = 6776
singles_raw = (42039 - doubles - triples - home_runs)
walks_raw = 15895
strike_outs_raw = 42823
hit_by_pitch_raw = 1984
outs_raw = (plate_apperances_raw - hits_raw - walks_raw - hit_by_pitch_raw - strike_outs_raw)

# These are the 2019 random batting percentages.
single_probability = singles_raw / plate_apperances_raw
double_probability = doubles_raw / plate_apperances_raw
triple_probability = triples_raw / plate_apperances_raw
home_run_probability = home_runs_raw / plate_apperances_raw
walk_probability = walks_raw / plate_apperances_raw
strike_out_probability = strike_outs_raw / plate_apperances_raw
hit_by_pitch_probability = hit_by_pitch_raw / plate_apperances_raw
out_probability = outs_raw / plate_apperances_raw

print(single_probability + double_probability + triple_probability + home_run_probability + walk_probability + strike_out_probability + hit_by_pitch_probability + out_probability)

# This will decide the play outcome.

# This will count the play outcome result
def count_play_result(play_outcome):
    if batted_single:
        hit = hit + 1