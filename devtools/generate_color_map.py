colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "bright_black", "bright_red", "bright_green", "bright_yellow", "bright_blue", "bright_magenta", "bright_cyan", "bright_white"]
print("self.color_map = {\n")
for color1 in colors:
    print(f"    \"{color1}\": self.term.{color1},")
    for color2 in colors:
        print(f"    \"{color1}_on_{color2}\": self.term.{color1}_on_{color2},")
print("}")