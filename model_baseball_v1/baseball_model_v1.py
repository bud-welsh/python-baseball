

# Here are the 2019 raw batting variables.
plate_apperances_raw = 186518
at_bats_raw = 166651
hits_raw = 42039
doubles_raw = 8531
triples_raw = 785
home_runs_raw = 6776
singles_raw = (42039 - doubles_raw - triples_raw - home_runs_raw)
walks_raw = 15895
strike_outs_raw = 42823
hit_by_pitch_raw = 1984
outs_raw = (plate_apperances_raw - hits_raw - walks_raw - hit_by_pitch_raw - strike_outs_raw)

# These are the 2019 batting probability functions.
def single_probability(singles_raw, plate_apperances_raw):
    return singles_raw / plate_apperances_raw

def double_probability(doubles_raw, plate_apperances_raw):
    return doubles_raw / plate_apperances_raw

def triple_probability(triples_raw, plate_apperances_raw):
    return triples_raw / plate_apperances_raw

def home_run_probability(home_runs_raw, plate_apperances_raw):
    return home_runs_raw / plate_apperances_raw

def walk_probability(walks_raw, plate_apperances_raw):
    return walks_raw / plate_apperances_raw

def strike_out_probability(strike_outs_raw, plate_apperances_raw):
    return strike_outs_raw / plate_apperances_raw

def hit_by_pitch_probability(hit_by_pitch_raw, plate_apperances_raw):
    return hit_by_pitch_raw / plate_apperances_raw

def out_probability(outs_raw, plate_apperances_raw):
    return outs_raw / plate_apperances_raw

