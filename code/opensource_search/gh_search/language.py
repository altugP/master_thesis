import logging
import yaml


class LinguistData:
  '''
  Class that reads the linguist languages.yaml file that GitHub uses to
  determine the categories of each supported language.

  The [languages.yaml](https://github.com/github-linguist/linguist/blob/master/lib/linguist/languages.yml)
  file was downloaded from the official [github-linguist](https://github.com/github-linguist/)
  account on 2024-01-30.

  Attributes
  ----------
  file_path: str
    String path to the downloaded local copy of languages.yaml.
  lookup_table: dict
    Dictionary containing information about every supported language of GitHub
    and whether GitHub considers that language a programming language or not.

  Methods
  -------
  _read_linguist_data() -> dict
    Reads the specified language file and returns its contents as a dict.
  _build_loopuk_table() -> dict
    Builds a dict that contains each supported language string as key and
    states if that language is a programming language as bool value.
  is_programming_language(language: str) -> bool
    Returns true if the given language tag (as used by GitHub, case-sensitive)
    is categorized as programming language.

  Examples
  --------
  ```py
  from language import *

  lang = LinguistData()
  print(lang.is_programming_language('TeX'))  # False, TeX is a markup language
  print(lang.is_programming_language('Kotlin'))  # True
  ```
  '''

  def __init__(self, file_path: str = 'config/languages.yaml'):
    self._file_path: str = file_path
    self._lookup_table: dict = self._build_loopuk_table()

  def _read_linguist_data(self) -> dict:
    '''Reads the languages.yaml file and returns the contents as dict.'''
    with open(self._file_path, 'r', encoding='utf-8') as file:
      linguist_data: dict = yaml.safe_load(file)
    return linguist_data

  def _build_loopuk_table(self) -> dict:
    '''
    Builds a dict that contains each supported language string as key and
    states if that language is a programming language as bool value.
    '''
    raw: dict = self._read_linguist_data()
    lookup_table: dict = {}
    for lang in raw.keys():
      lookup_table.update({lang: raw[lang]['type'] == 'programming'})
    return lookup_table

  def is_programming_language(self, language: str) -> bool:
    '''
    Returns true if the given language string is categorized as programming
    language by GitHub. Otherwise this returns false.

    Parameters
    ----------
    language: str
      The language tag as used by GitHub on their website or in their API
      responses e.g. C++ has the tag "C++", using "cpp" or "c++" will result in
      a False even though C++ is a supported language.

    Returns
    -------
    bool
      True if the language tag corresponds with a language that GitHub
      classifies as programming language. False if the language is not supported
      or is a non-programming language e.g. markup languages.
    '''
    if language not in self._lookup_table.keys():
      logging.getLogger('search_logger').warning(f'"{language}" not found in '
                                                 'GitHub languages file')
      return False
    return self._lookup_table[language]
