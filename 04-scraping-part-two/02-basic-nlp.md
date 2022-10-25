# Natural Language Processing (NLP)

*NOTE: This is an EXTREMELY meagre overview of a few things you can do with spaCy. For more, see [spaCy 101](https://spacy.io/usage/spacy-101), and/or Allison Parrish's tutorial [NLP Concepts with spaCy](https://gist.github.com/aparrish/f21f6abbf2367e8eb23438558207e1c3).*

At its core, natural language processing (or NLP) systems allow the computer to "make sense" of human language. NLP tasks might include: determining that a particular set of characters is a word or a sentence; determining that a particular word is a noun, adjective or other part of speech; determining that a word is a "named entity" like a business, place, or person; estimating the similarity between two words or phrases. And so on!

[spaCy](https://spacy.io/usage/spacy-101) is a wonderful open source library that allows you to perform the above tasks, and more. 

### Installation

To install it, open up a terminal and type:

```bash
pip3 install spacy
```

You'll also need to install a language model. I'll be using English here, but other models are also [available](https://spacy.io/usage):

```bash
python3 -m spacy download en_core_web_sm
```

*Note: I'm using the "small" model which is fast, but less accurate.*

### Basic Usage

To use spaCy just, load up the library and the model, and then pass it some text to analyze:

```python
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("A spectre is haunting Europe. The spectre of communism.")

for token in doc:
    print(token.text, token.pos_, token.tag_)
```

The output will be:

```bash
A DET DT
spectre NOUN NN
is AUX VBZ
haunting VERB VBG
Europe PROPN NNP
. PUNCT .
The DET DT
spectre NOUN NN
of ADP IN
communism NOUN NN
. PUNCT .
```

`doc` is an iterator containing spaCy `Token` objects. Each token is a word or piece of punctuation, annotated with attributes that give you additional info about that token's grammatical structure. Here, we're printing out the text of each token, along with its coarse-grained (`.pos_`) and fine-grained (`.tag_`) part of speech tag. 

The possible [parts of speech (coarse-grained)](https://universaldependencies.org/u/pos/) are:

* ADJ: adjective
* ADP: adposition
* ADV: adverb
* AUX: auxiliary
* CCONJ: coordinating conjunction
* DET: determiner
* INTJ: interjection
* NOUN: noun
* NUM: numeral
* PART: particle
* PRON: pronoun
* PROPN: proper noun
* PUNCT: punctuation
* SCONJ: subordinating conjunction
* SYM: symbol
* VERB: verb
* X: other

The fine-grained `.tag_` annotation provides more specific details, such as verb form. A full list of those tags [can be found here](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).

So, if we want to extract all the nouns from a text we can simply select the words whose `.pos_` tag is equal to `"NOUN"`:

```python
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("A spectre is haunting Europe. The spectre of communism.")

nouns = [token.text for token in doc if token.pos_ == "NOUN"]
print(nouns)
```

The output would be: `['spectre', 'spectre', 'communism']`.

*NOTE: you can extract sentences from a spaCy doc with `doc.sents`.*


### Pattern Matching

`spaCy` also has a great system for finding phrases that match specific grammatical patterns in texts. It's sort of like regex but for grammar. spaCy has [extensive documentation](https://explosion.ai/demos/matcher) on their matcher, as well as an [interactive tool](https://explosion.ai/demos/matcher) to explore the matcher rules, so this is, again, just a very brief intro!

Let's say that we want to extract all the phrases from the Communist Manifesto that match the pattern `determiner adjective noun`. These are phrases like "a holy alliance" and "the modern State". 

```python
import spacy
from spacy.matcher import Matcher

# load spacy and create a matcher object
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# a list of patterns to look for
patterns = [
    [{"POS": "DET"}, {"POS": "ADJ"}, {"POS": "NOUN"}]],
]

matcher.add("MyPattern", patterns)

# read in the communist manifesto
doc = nlp(open("manifesto.txt").read())

# find matches
matches = matcher(doc)

# print the text of the matches
for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)

```

*Note: the matcher returns a start and end index for each match. In order to actually get the text of the matches, we feed those indices to our doc object.*

*Note: if you want to use fine-grained tags, just write `"TAG"` instead of `"POS"`.*

Here are a few other examples of patterns.

"determiner adjective noun adposition noun", i.e. "the present system of production":

```python
[{"POS": "DET"}, {"POS": "ADJ"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}]
```

"determiner noun be adjective", i.e. "the workers are victorious":

```python
[{"POS": "DET"}, {"POS": "NOUN"}, {"LEMMA": "be"}, {"POS": "ADJ"}]
```

### Similarity

You can also use spaCy to determine the similarity between words and phrases. Each `doc` and `token` object contains a `similarity` function that takes as an argument any other `doc` or `token`, and will return as estimate of semantic similarity between the words. 

To use this, you must first download spaCy's larger language model:

```bash
python -m spacy download en_core_web_lg
```

Then you can iterate through spaCy objects and determine similarity:


```python
import spacy

# load the larger language model
nlp = spacy.load("en_core_web_lg")

# search for words similar to "money"
search_sim = nlp("money")

doc = nlp(open("manifesto.txt").read())
for s in doc.sents:
   sim = search_sim.similarity(s)
   print(s, sim)   
```
