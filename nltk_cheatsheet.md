## NLTK Book
  

* Texts are represented in Python using lists: `['Monty', 'Python']`. We can use indexing, slicing, and the `len()` function on lists.
*    A word "token" is a particular appearance of a given word in a text; a word "type" is the unique form of the word as a particular sequence of letters. We count word tokens using `len(text)` and word types using `len(set(text))`.
*    We obtain the vocabulary of a text `t` using `sorted(set(t))`.
*    We operate on each item of a text using `[f(x) for x in text]`.
*    To derive the vocabulary, collapsing case distinctions and ignoring punctuation, we can write `set(w.lower() for w in text if w.isalpha())`.
*    We process each word in a text using a for statement, such as `for w in t:` or `for word in text:`. This must be followed by the colon character and an indented block of code, to be executed each time through the loop.
*    We test a condition using an if statement: `if len(word) < 5:`. This must be followed by the colon character and an indented block of code, to be executed only if the condition is true.
*    A frequency distribution is a collection of items along with their frequency counts (e.g., the words of a text and their frequency of appearance).
*    A function is a block of code that has been assigned a name and can be reused. Functions are defined using the def keyword, as in `def mult(x, y);` x and y are parameters of the function, and act as placeholders for actual data values.
*    A function is called by specifying its name followed by zero or more arguments inside parentheses, like this: `texts()`, `mult(3, 4)`, `len(text1)`.

  
![dialogue workflow](http://www.nltk.org/images/dialogue.png)  


*    In this book we view a text as a list of words. A "raw text" is a potentially long string containing words and whitespace formatting, and is how we typically store and visualize a text.
*    A string is specified in Python using single or double quotes: `'Monty Python'`, `"Monty Python"`.
*    The characters of a string are accessed using indexes, counting from zero: `'Monty Python'[0]` gives the value M. The length of a string is found using `len()`.
*    Substrings are accessed using slice notation: `'Monty Python'[1:5]` gives the value `onty`. If the start index is omitted, the substring begins at the start of the string; if the end index is omitted, the slice continues to the end of the string.
*    Strings can be split into lists: `'Monty Python'.split()` gives `['Monty', 'Python']`. Lists can be joined into strings: `'/'.join(['Monty', 'Python'])` gives `'Monty/Python'`.
*    We can read text from a file `input.txt` using `text = open('input.txt').read()`. We can read text from url using `text = request.urlopen(url).read().decode('utf8')`. We can iterate over the lines of a text file using `for line in open(f)`.
*    We can write text to a file by opening the file for writing `output_file = open('output.txt', 'w')`, then adding content to the file `print("Monty Python", file=output_file)`.
*    Texts found on the web may contain unwanted material (such as headers, footers, markup), that need to be removed before we do any linguistic processing.
*    Tokenization is the segmentation of a text into basic units — or tokens — such as words and punctuation. Tokenization based on whitespace is inadequate for many applications because it bundles punctuation together with words. NLTK provides an off-the-shelf tokenizer `nltk.word_tokenize()`.
*    Lemmatization is a process that maps the various forms of a word (such as appeared, appears) to the canonical or citation form of the word, also known as the lexeme or lemma (e.g. appear).
*    Regular expressions are a powerful and flexible method of specifying patterns. Once we have imported the re module, we can use `re.findall()` to find all substrings in a string that match a pattern.
*    If a regular expression string includes a backslash, you should tell Python not to preprocess the string, by using a raw string with an r prefix: `r'regexp'`.
*    When backslash is used before certain characters, e.g. `\n`, this takes on a special meaning (newline character); however, when backslash is used before regular expression wildcards and operators, e.g. `\.`, `\|`, `\$`, these characters lose their special meaning and are matched literally.
*    A string formatting expression template `% arg_tuple` consists of a format string template that contains conversion specifiers like `%-6s` and `%0.2d`.
