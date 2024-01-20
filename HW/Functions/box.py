import math

items = int(input("How many items need to be packed?\n"))
per_box = int(input("How many items per box?\n"))

box = items / per_box

print(f"For {items} items, packing {per_box} items per box, you will need {math.ceil(box)} boxes.")