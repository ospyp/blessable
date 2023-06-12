# Blesser

Blesser is a simple library powered by the Blessed library. Blesser adds a simple markup language that has a similar syntax to HTML.

## Support

Through Blessed, Blesser supports almost all platforms:

 - Windows `NEW`
 - macOS
 - Linux
 - BSD

Please refer to the Blessed documentation for more information.

## Usage

First, import the `blesser` module:

```python
from blesser import Blesser
```

Then, use `blesser` like this:

```python
blesser = Blesser()
print(blesser.bless('<green>Success</green> - <blue_on_white>Blesser has been installed!</blue_on_white>'))
```

Try it out!

### Blesser Markup Language

Blesser Markup Language is a simple markup language similar to HTML.

```html
Text <color>text</color> text
```

Demo:

```html
The Blessed library is truly <red>amazing</red>, with <blue>Windows, Mac, and Linux Support</blue> all built-in!
```

## Supported Colors

The following colors are supported, as well as `color_on_color`, e.g. `white_on_blue`:

 - `black`
 - `red`
 - `green`
 - `yellow`
 - `blue`
 - `magenta`
 - `cyan`
 - `white`
 - `bright_black`
 - `bright_red`
 - `bright_green`
 - `bright_yellow`
 - `bright_blue`
 - `bright_magenta`
 - `bright_cyan`
 - `bright_white`

In addition to these colors, we also supports the following non-colors:

 - `bold` (alias `b`)
 - `italic` (alias `i`)
 - `underline` (alias `u`)

## To Do

 - [ ] Support nested styling