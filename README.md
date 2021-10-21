# spanish_inflections

Identify and change the gender and number of adjetives and nouns in spanish.

## How to use?

### Adjetives

```python
from spanish_inflections import search_adjetive
adjetive = "grandes"
search_adjetive(adjetive)

# OUTPUTS
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
search_noun(noun)

# OUTPUTS
'''
{'original': 'perro', 'MS': 'perro', 'MP': 'perros'}
'''
```

For more details check examples.ipynb
