from .colormap import color_map

class Blesser:
    # def __init__(self):
        # self.term = Terminal()

    def bless(self, markup):
        parts = markup.split('<')
        converted_markup = []

        for part in parts:
            if '>' in part:
                color_tag, text = part.split('>', 1)
                color_tag = color_tag.strip()

                if color_tag in color_map:
                    converted_markup.append(color_map[color_tag](text))
                else:
                    converted_markup.append(text)
            else:
                converted_markup.append(part)

        return ''.join(converted_markup)