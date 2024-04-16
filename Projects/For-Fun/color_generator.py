import random

# Extensive color database
colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", 
    "cyan", "magenta", "teal", "olive", "maroon", "navy", "indigo", "turquoise", 
    "lavender", "silver", "gray", "black", "white", "crimson", "gold", "violet", 
    "peach", "ruby", "emerald", "sapphire", "amber", "coral", "ivory", "plum", 
    "salmon", "taupe", "azure", "chartreuse", "khaki", "mauve", "scarlet", "turquoise",
    "beige", "aquamarine", "peridot", "cerulean", "lilac", "mustard", "russet", 
    "vermilion", "amethyst", "fuchsia", "tangerine", "orchid", "cobalt", "celadon",
    "eggplant", "sepia", "lemon", "peacock", "berry", "copper", "steel", "melon",
    "mahogany", "topaz", "rose", "seafoam", "ruby", "champagne", "burgundy", 
    "sky blue", "mint green", "forest green", "tan", "cream", "taupe", "aubergine",
    "olive green", "honey", "caramel", "mauve", "salmon pink", "lavender", "slate gray",
    "baby blue", "powder blue", "lavender", "teal green", "pumpkin", "marigold",
    "emerald green", "sea green", "brick red", "sky blue", "chocolate", "vanilla",
    "sienna", "pea green", "eggshell", "rust", "teal blue", "steel blue", "navajo white",
    "periwinkle", "orchid", "moccasin", "linen", "bisque", "papaya whip", "cornflower blue",
    "lavender blush", "light salmon", "pale turquoise", "light steel blue", "light coral",
    "rosy brown", "light sky blue", "light green", "light yellow", "light pink", "light goldenrod",
    "light blue", "light gray", "dark red", "dark green", "dark blue", "dark yellow", "dark orange",
    "dark purple", "dark pink", "dark brown", "dark cyan", "dark magenta", "dark teal", "dark olive",
    "dark maroon", "dark navy", "dark indigo", "dark turquoise", "dark lavender", "dark gray", "light slate gray"
]

def random_color():
    return random.choice(colors)

# Example usage
print("Random Color:", random_color())
