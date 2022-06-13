### Python application that calculates the optimal word path between a starting and an ending word of the same length, by changing one character in every step and always result to a valid English word.

### Word list is taken from https://github.com/dwyl/english-words.

### Word List assumptions:
1. All lowercase
2. No symbols
3. No spaces

### Example:
```commandline
pip install -r requirements.txt
```

```python
import json
from WordLadder import WordLadder

with open("word_list.json") as f:
    word_list = json.load(f)

my_word_ladder = WordLadder(word_list)
my_word_ladder.starting_word = "wheat"
my_word_ladder.ending_word = "bread"

my_word_ladder.find_shortest_word_ladder()
```

```
Depth:0, Nodes:['wheat']
Depth:1, Nodes:['cheat', 'sheat', 'theat', 'wheal', 'wheam', 'wheft', 'whewt', 'wreat']
Depth:2, Nodes:['cheap', 'cheet', 'chert', 'chest', 'cleat', 'creat', 'sceat', 'sheaf', 'sheal', 'shean', 'shear', 'sheas', 'sheet', 'shent', 'shoat', 'skeat', 'sweat', 'theah', 'theet', 'theft', 'treat', 'pheal', 'wheel', 'whewl', 'wheem', 'whelm', 'whift', 'whews', 'great', 'wreak', 'wrest']
Depth:3, Nodes:['aheap', 'cheep', 'chelp', 'cheek', 'cheer', 'chuet', 'chart', 'chera', 'chere', 'chirt', 'chort', 'chese', 'chess', 'crest', 'bleat', 'clead', 'cleam', 'clean', 'clear', 'cleft', 'clept', 'pleat', 'cread', 'creak', 'cream', 'crept', 'croat', 'scent', 'sclat', 'scrat', 'shelf', 'shraf', 'sheel', 'shell', 'sheol', 'shoal', 'speal', 'steal', 'sweal', 'sheen', 'shewn', 'skean', 'spean', 'stean', 'sheer', 'smear', 'spear', 'swear', 'rheas', 'sheds', 'shews', 'sheep', 'skeet', 'sleet', 'sweet', 'ghent', 'shant', 'shend', 'sheng', 'shunt', 'slent', 'spent', 'stent', 'suent', 'shoad', 'shoot', 'short', 'shott', 'shout', 'sloat', 'stoat', 'swelt', 'swept', 'theek', 'theer', 'tweet', 'thoft', 'tread', 'treas', 'trent', 'trest', 'troat', 'phial', 'jheel', 'wheen', 'wheep', 'wheer', 'whalm', 'whelk', 'whelp', 'shift', 'whiff', 'whipt', 'whist', 'chews', 'thews', 'wheys', 'whens', 'whets', 'greet', 'greit', 'grewt', 'groat', 'break', 'freak', 'wreck', 'arest', 'brest', 'drest', 'prest', 'weest', 'wrast', 'wrist']
Depth:4, Nodes:['ahead', 'creep', 'chela', 'check', 'cleek', 'creek', 'cheir', 'cruet', 'chaft', 'chait', 'chant', 'chapt', 'chara', 'chard', 'chare', 'chary', 'chark', 'charm', 'charr', 'chars', 'clart', 'coart', 'whart', 'cheka', 'chena', 'chora', 'cheke', 'cheve', 'chore', 'there', 'where', 'chint', 'chiot', 'chirk', 'chirl', 'chirm', 'chiro', 'chirp', 'chirr', 'chiru', 'shirt', 'thirt', 'chord', 'chott', 'chout', 'thort', 'whort', 'chase', 'chose', 'chuse', 'these', 'chass', 'chefs', 'cress', 'ghess', 'cresc', 'cryst', 'crost', 'crust', 'bleak', 'blear', 'blent', 'blest', 'bloat', 'glead', 'plead', 'cloam', 'fleam', 'gleam', 'elean', 'glean', 'flear', 'aleft', 'clefs', 'clift', 'clapt', 'clepe', 'clipt', 'slept', 'pleas', 'ploat', 'aread', 'bread', 'creed', 'dread', 'oread', 'croak', 'bream', 'creem', 'dream', 'fream', 'crepe', 'crepy', 'crypt', 'erept', 'croft', 'crout', 'scant', 'scena', 'scend', 'scene', 'eclat', 'salat', 'sclav', 'sclaw', 'splat', 'scrab', 'scrae', 'scrag', 'scray', 'scram', 'scran', 'scrap', 'scraw', 'scrit', 'sprat', 'surat', 'shela', 'sheld', 'shilf', 'skelf', 'saraf', 'shrab', 'shrag', 'shram', 'shrap', 'shiel', 'skeel', 'speel', 'steel', 'shall', 'shill', 'skell', 'smell', 'snell', 'spell', 'stell', 'swell', 'shool', 'theol', 'shorl', 'skoal', 'speak', 'speil', 'spial', 'stead', 'steak', 'steam', 'rheen', 'skeen', 'speen', 'steen', 'shawn', 'shewa', 'shown', 'skein', 'stein', 'stern', 'styan', 'shier', 'shyer', 'shoer', 'skeer', 'sleer', 'smeer', 'sneer', 'speer', 'steer', 'sweer', 'speir', 'rheae', 'seeds', 'shads', 'shedu', 'sleds', 'sneds', 'shaws', 'shows', 'skews', 'slews', 'smews', 'spews', 'stews', 'shlep', 'sleep', 'steep', 'sweep', 'skeed', 'skeeg', 'skees', 'fleet', 'gleet', 'sleek', 'glent', 'shaft', 'shalt', 'shane', 'shang', 'shank', 'slant', 'suant', 'sherd', 'spend', 'stend', 'cheng', 'steng', 'ahunt', 'saunt', 'shune', 'shuns', 'stunt', 'olent', 'spect', 'spekt', 'spelt', 'steno', 'stept', 'stert', 'stint', 'quent', 'suint', 'scoad', 'shoed', 'shood', 'showd', 'bhoot', 'scoot', 'sfoot', 'shooi', 'shook', 'shoon', 'shoop', 'shoor', 'shoos', 'skoot', 'sloot', 'smoot', 'snoot', 'spoot', 'stoot', 'whoot', 'shore', 'shorn', 'snort', 'sport', 'ssort', 'scott', 'shote', 'shots', 'stott', 'scout', 'skout', 'smout', 'snout', 'spout', 'stout', 'float', 'gloat', 'sloan', 'stoae', 'stoai', 'stoas', 'stoit', 'stopt', 'dwelt', 'smelt', 'svelt', 'swelp', 'their', 'theor', 'tweed', 'tweeg', 'tweel', 'tween', 'thowt', 'troft', 'treed', 'trend', 'triad', 'troad', 'areas', 'oreas', 'trees', 'treys', 'treks', 'tress', 'trets', 'trews', 'trias', 'ureas', 'arent', 'brent', 'drent', 'trant', 'urent', 'teest', 'trist', 'tryst', 'trust', 'troak', 'troot', 'trout', 'phill', 'whein', 'whale', 'whaly', 'whalp', 'whilk', 'whulk', 'shipt', 'shist', 'skift', 'smift', 'snift', 'swift', 'whuff', 'whips', 'waist', 'whish', 'whisk', 'whisp', 'whiss', 'chaws', 'chewy', 'chows', 'clews', 'crews', 'thaws', 'thens', 'theos', 'thewy', 'weens', 'whins', 'wrens', 'weets', 'whats', 'whits', 'freet', 'greed', 'greek', 'green', 'grees', 'freit', 'gleit', 'grein', 'groan', 'gront', 'groot', 'grout', 'breck', 'breek', 'fleak', 'freck', 'dreck', 'wrack', 'wrick', 'arist', 'awest', 'beest', 'brast', 'brett', 'brist', 'doest', 'dress', 'piest', 'presa', 'prese', 'press', 'prost', 'feest', 'geest', 'keest', 'reest', 'weent', 'weesh', 'wrapt', 'frist', 'grist']

Solution ladder: wheat -> cheat -> creat -> cread -> bread
Steps required: 4
Nodes visited: 531
```