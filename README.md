# Word
This repo will hold the Word class and associated functions for statistical NLP.

To use this class simply call:

`test = Word("test")`

This will store the word "test" inside the Word object. You can access the word and all its attributed by using commands like:

```
test.synonyms
test.definitionList
```

The Word class currently contains the following attributes useful in NLP:

`text`: which contains the initializing word.

`synonyms`: A list of synonyms based on WordNet.

`antonyms`: A list of antonyms based on WordNet.

`pos`: The WordNet part of speech tag.

`definitionDict`: A dictionary of definitions, keyed on the WordNet synonym set.

`soundex`: The soundex representation of the word's text attribute.

`lemma` : The lemma of the word
