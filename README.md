# Pig Latin Translator

> Translator that converts English to Pig Latin using Python

## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Scope of Functionalities](#scope-of-functionalities)
- [Project Status](#project-status)
- [Contact](#contact)

## General info

### Pig Latin Rules

- If the word begins with a consonant, all letters before the first vowel are placed at the end of the word and "ay" is added
  - "pig" = "igpay"
  - "happy" = "appyhay"
  - "smile" = "ilesmay"
  - "trash" = "ashtray"
- If the word begins with a vowel, "way" is added
  - "eat" = "eatway"
  - "egg" = "eggway"
- If the letter "y" comes at the end of a consonant cluster, it should be treated like a vowel
  - "rhythm" = "ythmrhay"

#### When is "Y" a vowel or consonant

- [Reference](https://www.merriam-webster.com/words-at-play/why-y-is-sometimes-a-vowel-usage#:~:text=Y%20is%20considered%20to%20be,%2C%20deny%2C%20bicycle%2C%20acrylic.)
- Y is considered to be a vowel if
  - There is no other vowel (ex. gym, my)
  - The letter is at the end of a word or syllable (ex. candy, deny, bicycle, acrylic)
  - The letter is in the middle of a syllable (ex. system, borborygmus)

## Technologies

- Python 2.7

## Setup

```
# Clone this repository
$ git clone https://github.com/danakim21/pig-latin-translator.git

# Go into the repository
$ cd pig-latin-translator

# Open Python
$ python

# Import to_pig_latin function
>>> from main import to_pig_latin

# Use the translator
>>> to_pig_latin("pig")
'igpay'

>>> to_pig_latin("pig happy smile")
'igpay appyhay ilesmay'
```

## Scope of Functionalities

List of features ready

- Converts any word or sentences to Pig Latin

To Do

- Converting back to English from Pig Latin
- Build GUI for better usage

## Project Status

Project is: _temporarily finished_, will be updated for further development

## Contact

Created by [@danakim21](https://danakim21.github.io/) - feel free to contact me!
