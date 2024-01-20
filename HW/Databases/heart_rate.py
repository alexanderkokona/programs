# input
age = int(input("What is your age in years?\n"))

# calculate
max = 220 - age
min_ave = max * 0.65
max_ave = max * 0.85

# display
print(f"When you exercise to strengthen your heart, you should keep your heart rate beteen {min_ave:.0f} and {max_ave:.0f} beats per minute.")