# Blessable

Blessable is a simple library powered by the Blessed library. Blessable adds a simple markup language that has a similar syntax to HTML.

## Support

Through Blessed, Blessable supports almost all platforms:

 - Windows `NEW` (or not so new - came to the `blessed` library in 2019)
 - macOS
 - Linux
 - BSD

Please refer to the Blessed documentation for more information.

## Usage

**First, install the package:**

```python
pip install blessable # or python -m pip install blessable
```

Or, if you want the latest version of everything:

```python
pip install git+https://github.com/fakerybakery/blessable.git  # or python -m pip install git+https://github.com/fakerybakery/blessable.git
```

**Then, import the `blessable` module:**

```python
from blessable import Blessable
```

**Then, use `blessable` like this:**

```python
blessable = Blessable()
print(blessable.bless('<green>Success</green> - <blue_on_white>Blessable has been installed!</blue_on_white>'))
```

Try it out!

### Blessable Markup Language

Moved to our [Wiki](https://github.com/fakerybakery/blessable/wiki/Documentation#blessable-markup-language).

## API

There's only one function:

### `bless`

#### Usage

```
.bless(markup=String) -> String
```

#### Parameters

`markup`: `String` - the Blessable Markup Language markup

#### Returns

`String` - try printing this in your Terminal!

## Supported Colors

[Supported colors have been moved to our Wiki](https://github.com/fakerybakery/blessable/wiki/Documentation#supported-colors).

## To Do

 - [ ] Support nested styling
 - [ ] Support escaping tags

## Credits

Credits go to @jquast's amazing [blessed](https://github.com/jquast/blessed) library, a fork of @erikrose's [blessings](https://github.com/erikrose/blessings) library. Thanks also to ChatGPT for help with this codebase!

## FAQs

Please see the [Wiki](https://github.com/fakerybakery/blessable/wiki) for FAQs, comparisons, and more.

## Disclaimer
