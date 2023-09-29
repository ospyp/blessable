<!--
BLESSABLE OPEN-SOURCE "COPYLEFT" LICENSE, VERSION 2.0

Copyright (c) 2023, mrfakename. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. All advertising materials mentioning features or use of this software must display the following acknowledgement: This product includes software developed by mrfakename and the Blessable Contributors.
4. Neither the name of the mrfakename nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
5. You shall not engage in any activities, including but not limited to decompiling, reverse engineering, disassembling, or otherwise attempting to derive the source code from the provided binary distributions, except to the extent expressly permitted by applicable law.
6. Any redistributions, whether in source code or binary form, must include a copy of the original license terms, and the redistributed software must be subject to the same terms and conditions as set forth in this license.
7. Any changes, modifications, or enhancements made to the source code, whether by the original licensee or any subsequent distributor or contributor, must be made available under the same open source license as this software. Additionally, any redistributed code containing such changes or modifications must include clear and prominent attribution to the original authors and contributors of the software, as specified in the original copyright notice and license.
8. You may link or incorporate the software covered by this license into your own software, regardless of the license of your own software. When you do so, your software is not required to be subject to the same terms and conditions as set forth in this license. However, you must clearly and prominently inform users that your software includes software developed by mrfakename and the Blessable Contributors, and you must provide a copy of the original license terms of the linked or incorporated software.

By submitting code, issues, suggestions, or ideas ("Contributions") to this open source project, you hereby grant the author(s) of this software an irrevocable, worldwide, royalty-free license to use, reproduce, modify, sublicense, relicense, and distribute your Contributions for any purpose, including commercial purposes, under the terms of the open source license governing this project. You also acknowledge that the author(s) reserve the right to unilaterally change the project's license terms, and you agree that such changes will apply to your Contributions without the need for additional consent or notification. You further represent that you have the legal right to grant this license.

THIS SOFTWARE IS PROVIDED BY mrfakename/Blessable Contributors AS IS AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL mrfakename BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

THIS LICENSE MAY NOT BE USED FOR ANY OTHER PROGRAM OR SOFTWARE WITHOUT PRIOR WRITTEN PERMISSION FROM THE BLESSABLE AUTHORS.
-->

# Blessable

![PyPI - Downloads](https://img.shields.io/pypi/dm/blessable?color=blue&label=installs&logo=pypi&logoColor=white) ![PyPI](https://img.shields.io/pypi/v/blessable?color=blue&label=version&logo=pypi&logoColor=white) ![GitHub](https://img.shields.io/github/license/fakerybakery/blessable?color=blue&label=license&logo=github&logoColor=white) ![GitHub Repo stars](https://img.shields.io/github/stars/fakerybakery/blessable?color=blue&label=stargazers&logo=github&logoColor=white) ![GitHub forks](https://img.shields.io/github/forks/fakerybakery/blessable?color=blue&label=forks&logo=github&logoColor=white) ![GitHub watchers](https://img.shields.io/github/watchers/fakerybakery/blessable?color=blue&label=watchers&logo=github&logoColor=white) ![GitHub issues](https://img.shields.io/github/issues/fakerybakery/blessable?color=blue&logo=github&logoColor=white) ![GitHub pull requests](https://img.shields.io/github/issues-pr/fakerybakery/blessable?color=blue&label=pull%20requests&logo=github&logoColor=white) ![Supported platforms](https://img.shields.io/badge/platforms-macOS%2C%20Linux%2C%20Windows-blue) ![Star Me](https://img.shields.io/badge/star-me-blue)

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

## Blessable vs. Rich

For a complete analysis, please see [our FAQ](https://github.com/fakerybakery/blessable/wiki/FAQs#blessable-vs-rich), but here's a summary:

Rich is good if you want lots of features, but Blessable is good if you just want colors.

Parsing the same string one million times, Blessable is on average over 59 times faster than Rich.

## FAQs

Please see the [Wiki](https://github.com/fakerybakery/blessable/wiki) for FAQs, comparisons, and more.

## If you find this useful...

Please star this repository! It makes a huge difference.

## Disclaimer

I do not endorse Blessed, Blessings, or ChatGPT.

```
THE SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS, CONTRIBUTORS, OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. YOU ACKNOWLEDGE THAT THE ENTIRE RISK ARISING OUT OF THE USE OR PERFORMANCE OF THE SOFTWARE REMAINS WITH YOU. IN NO EVENT SHALL THE AUTHORS, CONTRIBUTORS, OR COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
```

## License

This package is licensed under a [permissive copyleft license](LICENSE) (The Blessable Open-Source "Copyleft" License, Version 2.0). This license is similar to the GPL license, but allows you to use this library in software with other licenses. Please refer to the [full license](LICENSE) for details.


---

A initiative of [Open Source PYthon Packages](https://github.com/ospyp).

<a href="https://github.com/ospyp"><img width="100" src="https://raw.githubusercontent.com/ospyp/ospyp/main/logo.svg"></a>
