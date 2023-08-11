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

(This is not a license, but simply a disclaimer. I'm planning to add an open-sourced license later)
