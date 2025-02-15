from typing import Optional

from .element import Element


def _create_html_element(tag: str):
    class HTMLElement(Element):
        def __init__(self, inner_html: Optional[str] = None, **kwargs) -> None:
            super().__init__(tag)
            self._text = inner_html
            self.props.update(**kwargs)
    return HTMLElement


a = _create_html_element('a')
abbr = _create_html_element('abbr')
acronym = _create_html_element('acronym')
address = _create_html_element('address')
area = _create_html_element('area')
article = _create_html_element('article')
aside = _create_html_element('aside')
audio = _create_html_element('audio')
b = _create_html_element('b')
basefont = _create_html_element('basefont')
bdi = _create_html_element('bdi')
bdo = _create_html_element('bdo')
big = _create_html_element('big')
blockquote = _create_html_element('blockquote')
br = _create_html_element('br')
button = _create_html_element('button')
canvas = _create_html_element('canvas')
caption = _create_html_element('caption')
cite = _create_html_element('cite')
code = _create_html_element('code')
col = _create_html_element('col')
colgroup = _create_html_element('colgroup')
data = _create_html_element('data')
datalist = _create_html_element('datalist')
dd = _create_html_element('dd')
del_ = _create_html_element('del')
details = _create_html_element('details')
dfn = _create_html_element('dfn')
dialog = _create_html_element('dialog')
div = _create_html_element('div')
dl = _create_html_element('dl')
dt = _create_html_element('dt')
em = _create_html_element('em')
embed = _create_html_element('embed')
fieldset = _create_html_element('fieldset')
figcaption = _create_html_element('figcaption')
figure = _create_html_element('figure')
footer = _create_html_element('footer')
form = _create_html_element('form')
h1 = _create_html_element('h1')
hgroup = _create_html_element('hgroup')
hr = _create_html_element('hr')
i = _create_html_element('i')
iframe = _create_html_element('iframe')
img = _create_html_element('img')
input_ = _create_html_element('input')
ins = _create_html_element('ins')
kbd = _create_html_element('kbd')
label = _create_html_element('label')
legend = _create_html_element('legend')
li = _create_html_element('li')
main = _create_html_element('main')
map_ = _create_html_element('map')
mark = _create_html_element('mark')
menu = _create_html_element('menu')
meter = _create_html_element('meter')
nav = _create_html_element('nav')
object_ = _create_html_element('object')
ol = _create_html_element('ol')
optgroup = _create_html_element('optgroup')
option = _create_html_element('option')
output = _create_html_element('output')
p = _create_html_element('p')
param = _create_html_element('param')
picture = _create_html_element('picture')
pre = _create_html_element('pre')
progress = _create_html_element('progress')
q = _create_html_element('q')
rp = _create_html_element('rp')
rt = _create_html_element('rt')
ruby = _create_html_element('ruby')
s = _create_html_element('s')
samp = _create_html_element('samp')
search = _create_html_element('search')
section = _create_html_element('section')
select = _create_html_element('select')
small = _create_html_element('small')
source = _create_html_element('source')
span = _create_html_element('span')
strong = _create_html_element('strong')
sub = _create_html_element('sub')
summary = _create_html_element('summary')
sup = _create_html_element('sup')
svg = _create_html_element('svg')
table = _create_html_element('table')
tbody = _create_html_element('tbody')
td = _create_html_element('td')
template = _create_html_element('template')
textarea = _create_html_element('textarea')
tfoot = _create_html_element('tfoot')
th = _create_html_element('th')
thead = _create_html_element('thead')
time = _create_html_element('time')
track = _create_html_element('track')
u = _create_html_element('u')
ul = _create_html_element('ul')
var = _create_html_element('var')
video = _create_html_element('video')
wbr = _create_html_element('wbr')
