# First half inning

for outs in range(0, 4):
    if outs < 3:
        print("Batter up!")
        print("Batter strikes out.")
        outs += 1
    else:
        print("That's the end of the half inning.")