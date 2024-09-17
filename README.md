# spanish_inflections

Identify and change the gender and number of adjectives, verbs and nouns in spanish.

## How it works?

This is a Python script that relies in a big list of spanish words and its [EAGLES tags](https://www.cs.upc.edu/~nlp/tools/parole-sp.html) taken from the [Freeling project](https://github.com/TALP-UPC/FreeLing/tree/master/data/es) to find information about the gender and number alternatives of adjetives and nouns.

## How to use?

### Adjetives

```python
from spanish_inflections import search_adjetive
adjetive = "grandes"
adjetive_details = search_adjetive(adjetive)
print(adjetive_details)

# OUTPUT
'''
{'original': 'grandes',
 'FS': 'grande',
 'FP': 'grandes',
 'MS': 'grande',
 'MP': 'grandes'}
'''
```

### Nouns

```python
from spanish_inflections import search_noun
noun = "perro"
noun_details = search_noun(noun)
print(noun_details)

# OUTPUT
'''
{'original': 'perro', 'MS': 'perro', 'MP': 'perros'}
'''
```

For more details check [examples.ipynb](https://github.com/mathigatti/spanish_inflections/blob/main/examples.ipynb). And you can find some fun applications in this course about [literature and coding](https://docs.google.com/document/d/e/2PACX-1vQUugllkjwgJi3tV_czOiBtw_mKahBUYI7ojj1E3LSWAmix0rAGXOThrExwCLm59NGjmcg08TPl1bWr/pub).

# References
- https://www.cs.upc.edu/~nlp/tools/parole-sp.html
- http://nlp.lsi.upc.edu/freeling/
- Related projects
  - https://github.com/Jacobe2169/Python-Inflector
  - https://github.com/bjascob/pyInflect
  - https://github.com/jaraco/inflect
