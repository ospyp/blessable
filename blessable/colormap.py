from blessed import Terminal
term = Terminal()
color_map = {
    "bold": term.bold,
    "italic": term.italic,
    "underline": term.underline,
    "b": term.bold,
    "i": term.italic,
    "u": term.underline,
    "black": term.black,
    "black_on_black": term.black_on_black,
    "black_on_red": term.black_on_red,
    "black_on_green": term.black_on_green,
    "black_on_yellow": term.black_on_yellow,
    "black_on_blue": term.black_on_blue,
    "black_on_magenta": term.black_on_magenta,
    "black_on_cyan": term.black_on_cyan,
    "black_on_white": term.black_on_white,
    "black_on_bright_black": term.black_on_bright_black,
    "black_on_bright_red": term.black_on_bright_red,
    "black_on_bright_green": term.black_on_bright_green,
    "black_on_bright_yellow": term.black_on_bright_yellow,
    "black_on_bright_blue": term.black_on_bright_blue,
    "black_on_bright_magenta": term.black_on_bright_magenta,
    "black_on_bright_cyan": term.black_on_bright_cyan,
    "black_on_bright_white": term.black_on_bright_white,
    "red": term.red,
    "red_on_black": term.red_on_black,
    "red_on_red": term.red_on_red,
    "red_on_green": term.red_on_green,
    "red_on_yellow": term.red_on_yellow,
    "red_on_blue": term.red_on_blue,
    "red_on_magenta": term.red_on_magenta,
    "red_on_cyan": term.red_on_cyan,
    "red_on_white": term.red_on_white,
    "red_on_bright_black": term.red_on_bright_black,
    "red_on_bright_red": term.red_on_bright_red,
    "red_on_bright_green": term.red_on_bright_green,
    "red_on_bright_yellow": term.red_on_bright_yellow,
    "red_on_bright_blue": term.red_on_bright_blue,
    "red_on_bright_magenta": term.red_on_bright_magenta,
    "red_on_bright_cyan": term.red_on_bright_cyan,
    "red_on_bright_white": term.red_on_bright_white,
    "green": term.green,
    "green_on_black": term.green_on_black,
    "green_on_red": term.green_on_red,
    "green_on_green": term.green_on_green,
    "green_on_yellow": term.green_on_yellow,
    "green_on_blue": term.green_on_blue,
    "green_on_magenta": term.green_on_magenta,
    "green_on_cyan": term.green_on_cyan,
    "green_on_white": term.green_on_white,
    "green_on_bright_black": term.green_on_bright_black,
    "green_on_bright_red": term.green_on_bright_red,
    "green_on_bright_green": term.green_on_bright_green,
    "green_on_bright_yellow": term.green_on_bright_yellow,
    "green_on_bright_blue": term.green_on_bright_blue,
    "green_on_bright_magenta": term.green_on_bright_magenta,
    "green_on_bright_cyan": term.green_on_bright_cyan,
    "green_on_bright_white": term.green_on_bright_white,
    "yellow": term.yellow,
    "yellow_on_black": term.yellow_on_black,
    "yellow_on_red": term.yellow_on_red,
    "yellow_on_green": term.yellow_on_green,
    "yellow_on_yellow": term.yellow_on_yellow,
    "yellow_on_blue": term.yellow_on_blue,
    "yellow_on_magenta": term.yellow_on_magenta,
    "yellow_on_cyan": term.yellow_on_cyan,
    "yellow_on_white": term.yellow_on_white,
    "yellow_on_bright_black": term.yellow_on_bright_black,
    "yellow_on_bright_red": term.yellow_on_bright_red,
    "yellow_on_bright_green": term.yellow_on_bright_green,
    "yellow_on_bright_yellow": term.yellow_on_bright_yellow,
    "yellow_on_bright_blue": term.yellow_on_bright_blue,
    "yellow_on_bright_magenta": term.yellow_on_bright_magenta,
    "yellow_on_bright_cyan": term.yellow_on_bright_cyan,
    "yellow_on_bright_white": term.yellow_on_bright_white,
    "blue": term.blue,
    "blue_on_black": term.blue_on_black,
    "blue_on_red": term.blue_on_red,
    "blue_on_green": term.blue_on_green,
    "blue_on_yellow": term.blue_on_yellow,
    "blue_on_blue": term.blue_on_blue,
    "blue_on_magenta": term.blue_on_magenta,
    "blue_on_cyan": term.blue_on_cyan,
    "blue_on_white": term.blue_on_white,
    "blue_on_bright_black": term.blue_on_bright_black,
    "blue_on_bright_red": term.blue_on_bright_red,
    "blue_on_bright_green": term.blue_on_bright_green,
    "blue_on_bright_yellow": term.blue_on_bright_yellow,
    "blue_on_bright_blue": term.blue_on_bright_blue,
    "blue_on_bright_magenta": term.blue_on_bright_magenta,
    "blue_on_bright_cyan": term.blue_on_bright_cyan,
    "blue_on_bright_white": term.blue_on_bright_white,
    "magenta": term.magenta,
    "magenta_on_black": term.magenta_on_black,
    "magenta_on_red": term.magenta_on_red,
    "magenta_on_green": term.magenta_on_green,
    "magenta_on_yellow": term.magenta_on_yellow,
    "magenta_on_blue": term.magenta_on_blue,
    "magenta_on_magenta": term.magenta_on_magenta,
    "magenta_on_cyan": term.magenta_on_cyan,
    "magenta_on_white": term.magenta_on_white,
    "magenta_on_bright_black": term.magenta_on_bright_black,
    "magenta_on_bright_red": term.magenta_on_bright_red,
    "magenta_on_bright_green": term.magenta_on_bright_green,
    "magenta_on_bright_yellow": term.magenta_on_bright_yellow,
    "magenta_on_bright_blue": term.magenta_on_bright_blue,
    "magenta_on_bright_magenta": term.magenta_on_bright_magenta,
    "magenta_on_bright_cyan": term.magenta_on_bright_cyan,
    "magenta_on_bright_white": term.magenta_on_bright_white,
    "cyan": term.cyan,
    "cyan_on_black": term.cyan_on_black,
    "cyan_on_red": term.cyan_on_red,
    "cyan_on_green": term.cyan_on_green,
    "cyan_on_yellow": term.cyan_on_yellow,
    "cyan_on_blue": term.cyan_on_blue,
    "cyan_on_magenta": term.cyan_on_magenta,
    "cyan_on_cyan": term.cyan_on_cyan,
    "cyan_on_white": term.cyan_on_white,
    "cyan_on_bright_black": term.cyan_on_bright_black,
    "cyan_on_bright_red": term.cyan_on_bright_red,
    "cyan_on_bright_green": term.cyan_on_bright_green,
    "cyan_on_bright_yellow": term.cyan_on_bright_yellow,
    "cyan_on_bright_blue": term.cyan_on_bright_blue,
    "cyan_on_bright_magenta": term.cyan_on_bright_magenta,
    "cyan_on_bright_cyan": term.cyan_on_bright_cyan,
    "cyan_on_bright_white": term.cyan_on_bright_white,
    "white": term.white,
    "white_on_black": term.white_on_black,
    "white_on_red": term.white_on_red,
    "white_on_green": term.white_on_green,
    "white_on_yellow": term.white_on_yellow,
    "white_on_blue": term.white_on_blue,
    "white_on_magenta": term.white_on_magenta,
    "white_on_cyan": term.white_on_cyan,
    "white_on_white": term.white_on_white,
    "white_on_bright_black": term.white_on_bright_black,
    "white_on_bright_red": term.white_on_bright_red,
    "white_on_bright_green": term.white_on_bright_green,
    "white_on_bright_yellow": term.white_on_bright_yellow,
    "white_on_bright_blue": term.white_on_bright_blue,
    "white_on_bright_magenta": term.white_on_bright_magenta,
    "white_on_bright_cyan": term.white_on_bright_cyan,
    "white_on_bright_white": term.white_on_bright_white,
    "bright_black": term.bright_black,
    "bright_black_on_black": term.bright_black_on_black,
    "bright_black_on_red": term.bright_black_on_red,
    "bright_black_on_green": term.bright_black_on_green,
    "bright_black_on_yellow": term.bright_black_on_yellow,
    "bright_black_on_blue": term.bright_black_on_blue,
    "bright_black_on_magenta": term.bright_black_on_magenta,
    "bright_black_on_cyan": term.bright_black_on_cyan,
    "bright_black_on_white": term.bright_black_on_white,
    "bright_black_on_bright_black": term.bright_black_on_bright_black,
    "bright_black_on_bright_red": term.bright_black_on_bright_red,
    "bright_black_on_bright_green": term.bright_black_on_bright_green,
    "bright_black_on_bright_yellow": term.bright_black_on_bright_yellow,
    "bright_black_on_bright_blue": term.bright_black_on_bright_blue,
    "bright_black_on_bright_magenta": term.bright_black_on_bright_magenta,
    "bright_black_on_bright_cyan": term.bright_black_on_bright_cyan,
    "bright_black_on_bright_white": term.bright_black_on_bright_white,
    "bright_red": term.bright_red,
    "bright_red_on_black": term.bright_red_on_black,
    "bright_red_on_red": term.bright_red_on_red,
    "bright_red_on_green": term.bright_red_on_green,
    "bright_red_on_yellow": term.bright_red_on_yellow,
    "bright_red_on_blue": term.bright_red_on_blue,
    "bright_red_on_magenta": term.bright_red_on_magenta,
    "bright_red_on_cyan": term.bright_red_on_cyan,
    "bright_red_on_white": term.bright_red_on_white,
    "bright_red_on_bright_black": term.bright_red_on_bright_black,
    "bright_red_on_bright_red": term.bright_red_on_bright_red,
    "bright_red_on_bright_green": term.bright_red_on_bright_green,
    "bright_red_on_bright_yellow": term.bright_red_on_bright_yellow,
    "bright_red_on_bright_blue": term.bright_red_on_bright_blue,
    "bright_red_on_bright_magenta": term.bright_red_on_bright_magenta,
    "bright_red_on_bright_cyan": term.bright_red_on_bright_cyan,
    "bright_red_on_bright_white": term.bright_red_on_bright_white,
    "bright_green": term.bright_green,
    "bright_green_on_black": term.bright_green_on_black,
    "bright_green_on_red": term.bright_green_on_red,
    "bright_green_on_green": term.bright_green_on_green,
    "bright_green_on_yellow": term.bright_green_on_yellow,
    "bright_green_on_blue": term.bright_green_on_blue,
    "bright_green_on_magenta": term.bright_green_on_magenta,
    "bright_green_on_cyan": term.bright_green_on_cyan,
    "bright_green_on_white": term.bright_green_on_white,
    "bright_green_on_bright_black": term.bright_green_on_bright_black,
    "bright_green_on_bright_red": term.bright_green_on_bright_red,
    "bright_green_on_bright_green": term.bright_green_on_bright_green,
    "bright_green_on_bright_yellow": term.bright_green_on_bright_yellow,
    "bright_green_on_bright_blue": term.bright_green_on_bright_blue,
    "bright_green_on_bright_magenta": term.bright_green_on_bright_magenta,
    "bright_green_on_bright_cyan": term.bright_green_on_bright_cyan,
    "bright_green_on_bright_white": term.bright_green_on_bright_white,
    "bright_yellow": term.bright_yellow,
    "bright_yellow_on_black": term.bright_yellow_on_black,
    "bright_yellow_on_red": term.bright_yellow_on_red,
    "bright_yellow_on_green": term.bright_yellow_on_green,
    "bright_yellow_on_yellow": term.bright_yellow_on_yellow,
    "bright_yellow_on_blue": term.bright_yellow_on_blue,
    "bright_yellow_on_magenta": term.bright_yellow_on_magenta,
    "bright_yellow_on_cyan": term.bright_yellow_on_cyan,
    "bright_yellow_on_white": term.bright_yellow_on_white,
    "bright_yellow_on_bright_black": term.bright_yellow_on_bright_black,
    "bright_yellow_on_bright_red": term.bright_yellow_on_bright_red,
    "bright_yellow_on_bright_green": term.bright_yellow_on_bright_green,
    "bright_yellow_on_bright_yellow": term.bright_yellow_on_bright_yellow,
    "bright_yellow_on_bright_blue": term.bright_yellow_on_bright_blue,
    "bright_yellow_on_bright_magenta": term.bright_yellow_on_bright_magenta,
    "bright_yellow_on_bright_cyan": term.bright_yellow_on_bright_cyan,
    "bright_yellow_on_bright_white": term.bright_yellow_on_bright_white,
    "bright_blue": term.bright_blue,
    "bright_blue_on_black": term.bright_blue_on_black,
    "bright_blue_on_red": term.bright_blue_on_red,
    "bright_blue_on_green": term.bright_blue_on_green,
    "bright_blue_on_yellow": term.bright_blue_on_yellow,
    "bright_blue_on_blue": term.bright_blue_on_blue,
    "bright_blue_on_magenta": term.bright_blue_on_magenta,
    "bright_blue_on_cyan": term.bright_blue_on_cyan,
    "bright_blue_on_white": term.bright_blue_on_white,
    "bright_blue_on_bright_black": term.bright_blue_on_bright_black,
    "bright_blue_on_bright_red": term.bright_blue_on_bright_red,
    "bright_blue_on_bright_green": term.bright_blue_on_bright_green,
    "bright_blue_on_bright_yellow": term.bright_blue_on_bright_yellow,
    "bright_blue_on_bright_blue": term.bright_blue_on_bright_blue,
    "bright_blue_on_bright_magenta": term.bright_blue_on_bright_magenta,
    "bright_blue_on_bright_cyan": term.bright_blue_on_bright_cyan,
    "bright_blue_on_bright_white": term.bright_blue_on_bright_white,
    "bright_magenta": term.bright_magenta,
    "bright_magenta_on_black": term.bright_magenta_on_black,
    "bright_magenta_on_red": term.bright_magenta_on_red,
    "bright_magenta_on_green": term.bright_magenta_on_green,
    "bright_magenta_on_yellow": term.bright_magenta_on_yellow,
    "bright_magenta_on_blue": term.bright_magenta_on_blue,
    "bright_magenta_on_magenta": term.bright_magenta_on_magenta,
    "bright_magenta_on_cyan": term.bright_magenta_on_cyan,
    "bright_magenta_on_white": term.bright_magenta_on_white,
    "bright_magenta_on_bright_black": term.bright_magenta_on_bright_black,
    "bright_magenta_on_bright_red": term.bright_magenta_on_bright_red,
    "bright_magenta_on_bright_green": term.bright_magenta_on_bright_green,
    "bright_magenta_on_bright_yellow": term.bright_magenta_on_bright_yellow,
    "bright_magenta_on_bright_blue": term.bright_magenta_on_bright_blue,
    "bright_magenta_on_bright_magenta": term.bright_magenta_on_bright_magenta,
    "bright_magenta_on_bright_cyan": term.bright_magenta_on_bright_cyan,
    "bright_magenta_on_bright_white": term.bright_magenta_on_bright_white,
    "bright_cyan": term.bright_cyan,
    "bright_cyan_on_black": term.bright_cyan_on_black,
    "bright_cyan_on_red": term.bright_cyan_on_red,
    "bright_cyan_on_green": term.bright_cyan_on_green,
    "bright_cyan_on_yellow": term.bright_cyan_on_yellow,
    "bright_cyan_on_blue": term.bright_cyan_on_blue,
    "bright_cyan_on_magenta": term.bright_cyan_on_magenta,
    "bright_cyan_on_cyan": term.bright_cyan_on_cyan,
    "bright_cyan_on_white": term.bright_cyan_on_white,
    "bright_cyan_on_bright_black": term.bright_cyan_on_bright_black,
    "bright_cyan_on_bright_red": term.bright_cyan_on_bright_red,
    "bright_cyan_on_bright_green": term.bright_cyan_on_bright_green,
    "bright_cyan_on_bright_yellow": term.bright_cyan_on_bright_yellow,
    "bright_cyan_on_bright_blue": term.bright_cyan_on_bright_blue,
    "bright_cyan_on_bright_magenta": term.bright_cyan_on_bright_magenta,
    "bright_cyan_on_bright_cyan": term.bright_cyan_on_bright_cyan,
    "bright_cyan_on_bright_white": term.bright_cyan_on_bright_white,
    "bright_white": term.bright_white,
    "bright_white_on_black": term.bright_white_on_black,
    "bright_white_on_red": term.bright_white_on_red,
    "bright_white_on_green": term.bright_white_on_green,
    "bright_white_on_yellow": term.bright_white_on_yellow,
    "bright_white_on_blue": term.bright_white_on_blue,
    "bright_white_on_magenta": term.bright_white_on_magenta,
    "bright_white_on_cyan": term.bright_white_on_cyan,
    "bright_white_on_white": term.bright_white_on_white,
    "bright_white_on_bright_black": term.bright_white_on_bright_black,
    "bright_white_on_bright_red": term.bright_white_on_bright_red,
    "bright_white_on_bright_green": term.bright_white_on_bright_green,
    "bright_white_on_bright_yellow": term.bright_white_on_bright_yellow,
    "bright_white_on_bright_blue": term.bright_white_on_bright_blue,
    "bright_white_on_bright_magenta": term.bright_white_on_bright_magenta,
    "bright_white_on_bright_cyan": term.bright_white_on_bright_cyan,
    "bright_white_on_bright_white": term.bright_white_on_bright_white,
}