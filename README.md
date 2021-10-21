# spanish_inflections

Identify and change the gender and number of adjetives and nouns in spanish.

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

For more details check [examples.ipynb](https://github.com/mathigatti/spanish_inflections/blob/main/examples.ipynb)
