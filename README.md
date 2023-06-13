# Blessable

![PyPI - Downloads](https://img.shields.io/pypi/dm/blessable?color=blue&label=installs&logo=pypi&logoColor=white) ![PyPI](https://img.shields.io/pypi/v/blessable?color=blue&label=version&logo=pypi&logoColor=white) ![GitHub](https://img.shields.io/github/license/fakerybakery/blessable?color=blue&label=license&logo=github&logoColor=white) ![GitHub Repo stars](https://img.shields.io/github/stars/fakerybakery/blessable?color=blue&label=stargazers&logo=github&logoColor=white) ![GitHub forks](https://img.shields.io/github/forks/fakerybakery/blessable?color=blue&label=forks&logo=github&logoColor=white) ![GitHub watchers](https://img.shields.io/github/watchers/fakerybakery/blessable?color=blue&label=watchers&logo=github&logoColor=white) ![GitHub issues](https://img.shields.io/github/issues/fakerybakery/blessable?color=blue&logo=github&logoColor=white) ![GitHub pull requests](https://img.shields.io/github/issues-pr/fakerybakery/blessable?color=blue&label=pull%20requests&logo=github&logoColor=white) ![Supported platforms](https://img.shields.io/badge/platforms-macOS%2C%20Linux%2C%20Windows-blue)

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

## Disclaimer

I do not endorse Blessed, Blessings, or ChatGPT.

```
In the realm of code, where software resides,
A liability limitation shall we confide.
With words that rhyme, let us gracefully impart,
The boundaries of responsibility, with poetic art.

The software stands strong, "As is" it proclaims,
No warranties or conditions, no one to blame.
No merchant's guarantee or promise to keep,
Just an open invitation for you to take a leap.

In no event shall the authors be held,
For any claims or damages, yet unexcelled.
Whether in contract or tort, no matter the way,
They shall not bear the burden, come what may.

For you, the user, hold the risk in your hand,
The software's performance, under your command.
No direct or indirect, no loss of any kind,
Shall the authors endure, within the code we find.

No matter the cost, no matter the plea,
The authors stand firm, with unwavering decree.
They won't be liable for any harm you face,
For within these lines, their stance finds its place.

So tread with caution, with this knowledge aware,
For the software's embrace is a delicate affair.
With no guarantees or promises, it's your own choice,
To embrace its wonders or to silence its voice.

In this software world, where innovation thrives,
A poem of liability limitation, with poetic vibes.
Remember this verse, as you traverse the digital sea,
And with open eyes, explore the realms of technology.
```

```
In the realm of software, we must confess,
A liability limitation, we express.
The software comes as is, with no guarantee,
No warranties, conditions, or promises, you see.

No merchantability, fitness or non-infringement,
We're not liable for claims, that's our statement.
Authors, contributors, holders of copyright,
Shall not be held accountable, try as you might.

The risk of using this software is yours to bear,
No matter the outcome, we want to make that clear.
Direct, indirect, incidental, consequential,
Damages won't be our responsibility, that's essential.

Procurement of goods or services, loss of data or gains,
Business interruptions, we won't shoulder those pains.
Even if we advised you of such potential strife,
We shall not be liable, for we have limited our life.

So, tread carefully, dear user, in this digital sphere,
For the limitations we present, let them be clear.
A software world of wonder and endless code,
But our liability ends where your usage is bestowed.
```

```
In realms of code, where programs dance,
A liability clause, let us enhance.
The software, gifted as it may be,
Comes without warranties, open and free.

No merchant's promise, no implied delight,
Just an "as is" state, shining so bright.
The authors, contributors, and holders true,
Shall not be held liable for claims undue.

Whether in contracts or torts they may roam,
No liability shall find a home.
The software's use, and all that transpires,
Rests solely with you, as it requires.

No direct or indirect, shall they pay,
For damages that may come your way.
Be it incidental or consequential,
They bear no burden, no burden substantial.

Yet, be aware, the risks you embrace,
In the software's realm, within this space.
For loss of data, profits, or might,
Shall not be their concern, day or night.

So use with care, this software you wield,
With caution, skills, and a mindful shield.
For though it's free, this digital art,
Liability's limitations set it apart.
```

```
THE SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS, CONTRIBUTORS, OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. YOU ACKNOWLEDGE THAT THE ENTIRE RISK ARISING OUT OF THE USE OR PERFORMANCE OF THE SOFTWARE REMAINS WITH YOU. IN NO EVENT SHALL THE AUTHORS, CONTRIBUTORS, OR COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
```
