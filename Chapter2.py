def Chapter2_1():
    print('2.1 Splitting Strings on Any of Multipler Delimiters')
    lines = 'adf fjdk; afed, fjek,asdf,      foo'

    import re
    res = re.split(r'[;,\s]\s*', lines)
    print(res)


def Chapter2_2():
    print('2.2 Matching Text at the Start or End of a String')
    print('\t Example 1')
    filename = 'spam.txt'
    print(filename)
    print('filename ends with .txt', filename.endswith('.txt'))
    print('filename starts with \'file\'', filename.startswith('file:'))
    url = 'http://www.python.org'
    print(url.startswith('http:'))

    filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
    print([name for name in filenames if name.endswith(('.c', '.h'))])

    print('note that string.startswith and string.endswith require a tuple')


def Chapter2_3():
    print('2.3 Matching String using Shell Wildcard patters')
    from fnmatch import fnmatch, fnmatchcase

    print('''fnmatch('foo.txt', '*.txt') >>>''', fnmatch('foo.txt', '*.txt'))
    print('''fnmatch('foo.txt', '?oo.txt') >>>''',
          fnmatch('foo.txt', '?oo.txt'))
    print('''fnmatch('Dat45.csv', 'Dat[0-9]*') >>>''',
          fnmatch('Dat45.csv', 'Dat[0-9]*'))

    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print('names =', names)
    print('''[name for name in names if fnmatch(name, 'Dat*csv')] >>>''',
          [name for name in names if fnmatch(name, 'Dat*csv')])
    print('''fnmatch('foo.txt', '*.TXT') >>>''', fnmatch('foo.txt', '*.TXT'))
    print('''fnmatchcase('foo.txt', '*.TXT') >>>''',
          fnmatchcase('foo.txt', '*.TXT'))


def Chapter2_4():
    print('2.4 Matching and Searching for Text Patterns')
    text = 'yeah, but no, but yeah, but no, but yeah'
    print('# Exact match')
    print('text = ', text)
    print('''text == 'yeah' >>>''', text == 'yeah')

    print('Match at start or end')
    print('''text.startswith('yeah') >>> ''', text.startswith('yeah'))
    print('''text.endswith('no') >>> ''', text.endswith('no'))

    print('\n\n# Search for the location of the first ocurrence')
    print('''text.find('no') >>> ''', text.find('no'))

    print('\n\n More complicated matching use re')
    import re
    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'
    print('text1 = ', text1)
    print('text2 = ', text2)

    print('# Simple matching, \d+ means match one or more digits')
    if re.match(r'\d+/\d+/\d+', text1):
        print('yes')
    else:
        print('no')

    print('precompile re first if going to do a lot of matches')
    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(text2):
        print('yes')
    else:
        print('no')

    print('re.match only matches at the beginning, use findall() for all occurences')
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
    print('text = ', text)
    print('datepat.findall(text) >>>', datepat.findall(text))

    print('using capture groups')
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print('''m = datepat.match('11/27/2012')''' )
    m = datepat.match('11/27/2012')
    print('m.group(0) >>>', m.group(0))
    print('m.group(1) >>>', m.group(1))
    print('m.group(2) >>>', m.group(2))
    print('m.group(3) >>>', m.group(3))
    print('m.groups() >>>', m.groups())


def Chapter2_5():
    print('2.5  Searching and Replacing Text')
    print('simple example')
    text = 'yeah, but no, but yeah, but no, but yeah'
    print('''text.replace('yeah', 'yep')''', text.replace('yeah', 'yep'))

    print('more complicated, using re')
    text = 'Today is 11/27/2012.  PyCon starts 3/13/2013'
    print('text = ', text)
    import re
    print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

    print('''using substitution callback functions in re.sub''')
    from calendar import month_abbr
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

    print('datepat.sub(change_date, text) >>>', datepat.sub(change_date, text))


def Chapter2_6():
    import re
    print('2.6 Searching and Replacing Case-Insensitive Text')
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print('''re.findall('python', text, flags=re.IGNORECASE) >>> ''',
          re.findall('python', text, flags=re.IGNORECASE))
    print('''re.sub('python', 'snake', text, flags=re.IGNORECASE) >>> ''',
          re.sub('python', 'snake', text, flags=re.IGNORECASE))

    def matchcase(word):
        def replace(m):
            text = m.group()
            if text.isupper():
                return word.upper()
            elif text.islower():
                return word.lower()
            elif text[0].isupper():
                return word.capitalize()
            else:
                return word
        return replace
    print('''re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE) >>> ''',
          re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))


def Chapter2_7():
    print('2.7 Specifying a Regular Expression for teh Shortest Match')
    import re
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    print('text1 = ', text1)
    print('str_pat.findall(text1) >>> ', str_pat.findall(text1))
    text2 = 'Computer says "no." Phone says "yes."'
    print('str_pat.findall(text2) >>> ', str_pat.findall(text2))
    print('not good, match is greedy')

    str_pat = re.compile(r'\"(.*?)\"')
    print('using ? operator in re')
    print(''' str_pat = re.compile(r'\"(.*?)\"')''')
    print('''str_pat.findall(text2) >>> ''', str_pat.findall(text2))


def Chapter2_8():
    import re
    print('2.8 Writing a Regular Expression for Multiline Patterns')
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/* this is a 
    multiline comment */
    '''
    print('text1 = ', text1)
    print('text2 = ', text2)
    print('''comment.findall(text1) >>> ''', comment.findall(text1))

    print('''comment.findall(text2) >>> ''', comment.findall(text2))

    print('''adding support for new line''')
    comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    print('''comment.findall(text2) >>> ''', comment.findall(text2))
    print('?: specifies a noncapture group')


def Chapter2_9():
    print('''2.9 Normalizing unicode text to a standard representation''')
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print('s1 = ', s1)
    print('ascii(s1) >>>', ascii(s1))
    print('ascii(s2) >>>', ascii(s2))

    print('s2 = ', s2)

    print('s1 == s2', s1 == s2)
    print('len(s1) >>>', len(s1))
    print('len(s2) >>>', len(s2))

    import unicodedata
    t1 = unicodedata.normalize('NFC', s1)
    print('''t1 = unicodedata.normalize('NFC', s1)''')
    t2 = unicodedata.normalize('NFC', s2)
    print('''t2 = unicodedata.normalize('NFC', s2)''')
    print('t1 >>>', t1)
    print('t2 >>>', t2)
    print('ascii(t1) >>>', ascii(t1))
    print('ascii(t2) >>>', ascii(t2))


def Chapter2_10():
    print('2.10 Working With unicode characters in regular expressions')
    import re
    num = re.compile('\d+')
    print('''num.match('123')''', num.match('123'))
    arabic_digits = '\u0661\u0662\u0663'
    print(arabic_digits)


def Chapter2_11():
    print('2.11 Stripping Unwanted Characters from Strings')
    print('stripping whitespace')
    s = '   hello world    \n'
    print('s = ', s)
    print('s.lstrip() >>>', s.lstrip())
    print('s.rstrip() >>>', s.rstrip())

    t = '-------hello======='
    print('t = ', t)
    print('''t.lstrip('-') >>>''', t.lstrip('-'))
    print('''tstrip('-=') >>> ''', t.strip('-='))


def Chapter2_12():
    print('2.12 Santizing and Cleaning up text')
    pass


def Chapter2_13():
    print('''2.13 Aligning Text Strings''')
    text = 'Hello World'
    print('text = ', text)
    print('text.ljust(20) >>>', text.ljust(20))
    print('text.rjust(20) >>>', text.rjust(20))
    print('text.center(20) >>>', text.center(20))
    print('text.ljust(20, \'=\') >>>', text.ljust(20, '='))
    print('text.rjust(20, \'=\') >>>', text.rjust(20, '='))
    print('text.center(20, \'=\') >>>', text.center(20, '='))
    print('using format function with >,<,^')
    print('format(text, \'>20\') >>>', format(text, '>20'))
    print('format(text, \'<20\') >>>', format(text, '<20'))
    print('format(text, \'^20\') >>>', format(text, '^20'))
    print('format(text, \'=>20\') >>>', format(text, '=>20'))
    print('format(text, \'=>20s\') >>>', format(text, '=>20s'))


def Chapter2_14():
    print('''2.15 Combinining and Concatenating Strings''')


def Chapter2_15():
    print('2.15 Interpolating Variables in Strings')
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))


def Chapter2_16():
    print('2.16 Reformatting Text to a Fixed Number of Columns')
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes"
    print(s)

    import textwrap
    print('textwrap.fill(s,40) >>> \n', textwrap.fill(s, 40))

def Chapter2_17():
    print('2.17 Handling HTML and XML Entities in Text')
    s = 'Elements are written as "<tag>text</tag>"'
    import html
    print('s = ', s)
    print('html.escape(s) >>>', html.escape(s))
    print('# Disable escaping of quotes')
    print('html.escape(s, quote=False) >>> ', html.escape(s, quote=False))

def Chapter2_18():
    print('2.18 Tokenizing Text')
    text = 'foo = 23 + 43 + 10'
    import re
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'

    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
    scanner = master_pat.scanner('foo = 23 + 42 * 10')
    match = scanner.match()
    print(match.lastgroup, match.group())

    for _ in range(12):
        match = scanner.match()
        print(match.lastgroup, match.group())

    from collections import namedtuple
    Token = namedtuple('Token', ['type', 'value'])
    def generate_tokens(pat, text):
        scanner = pat.scanner(text)
        for m in iter(scanner.match, None):
            yield Token(m.lastgroup, m.group())

    for tok in generate_tokens(master_pat, 'foo = 42'):
        print(tok)

if __name__ == "__main__":
    # Chapter2_1()
    # Chapter2_2()
    # Chapter2_3()
    # Chapter2_4()
    # Chapter2_5()
    # Chapter2_6()
    # Chapter2_7()
    # Chapter2_8()
    # Chapter2_9()
    # Chapter2_10()
    # Chapter2_11()
    # Chapter2_12()
    # Chapter2_13()
    # Chapter2_14()
    # Chapter2_15()
    # Chapter2_16()
    # Chapter2_17()
    Chapter2_18()
