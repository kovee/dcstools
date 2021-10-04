## ============================================================================
##                       ---=== DCS:World Tools ===---
##                  Copyright (C) 2021-2022, Attila Kovacs
## ============================================================================
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to
## deal in the Software without restriction, including without limitation the
## rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
## sell copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
## IN THE SOFTWARE.
##
## ============================================================================

"""Contains the implementation of the Localizer class."""

# Runtime Imports
import os
import logging
from string import Template

# Dependency Imports
import httpx
from ruamel.yaml import YAML
from googletrans import Translator

# DCS Imports
from dcs.constants import (
    DCSTOOLS_LOG_CHANNEL,
    LOCALIZER_SUPPORTED_LANGUAGES,
    DEFAULT_LOCALE,
    DEFAULT_LOCALIZATION_PATH
)

class Localizer:

    """Utility class to translate strings and fill in optional variables inside
    them.

    It also supports automatic translation of strings through the Google
    Translate API.

    The localizer will look for language files in the data/locale directory in
    the application's working directory by default. The default language is
    set to english, the startup language can be configured in the application's
    config file.
    """

    def __init__(
        self,
        default_language: str = DEFAULT_LOCALE,
        cache_default: bool = False,
        auto_translate: bool = False,
        localization_directory: str = DEFAULT_LOCALIZATION_PATH) -> None:

        """Creates a new Localizer instance.

        :param default_language: The default locale to use when looking for
            texts.
        :type default_language: str

        :param cache_default: Whether or not the default language file should
            also be loaded.
        :type cache_default: bool

        :param auto_translate: Automatically translate the text from the
            default language if no translated version was found.
        :type auto_translate: bool

        :param localization_directory: The directory in which the language
            files are located.
        :type localization_directory: str
        """

        self._language = default_language
        self._default_language = default_language
        self._auto_translate = auto_translate
        self._cache_default = cache_default
        self._data = None
        self._default_data = None
        self._localization_directory = localization_directory

        self._load_language_from_configuration()
        self._load_language_data()
        if self._cache_default:
            self._cache_default_language_data()

    def get(self, key: str, attributes: dict = None) -> str:

        """Retrieves the localized version of the given localization key and
        also fills any dynamic variables in the text.

        :param key: The localization key to retrieve.
        :type key: str

        :param attributes: Dictionary of dynamic attributes to substitute.
        :type attributes: dict

        :return: The localized string for the given key.
        :rtype: str
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Retrieving localized text for key {key}...')

        localized_text = None

        try:
            localized_text = self._data[key]
        except KeyError:
            logger.debug(
                f'Localization key {key} was not found in the current '
                f'language.')
            localized_text = self._load_default_text(key=key)
            if self._auto_translate:
                logger.debug(
                    f'Attempting to translate {key}({localized_text}) '
                    f'to language {self._language}.')
                localized_text = self._translate_text(text=localized_text)
                logger.debug(
                    f'Received translation for {key}: {localized_text}')

        if attributes is not None:
            logger.debug(f'Substituting supplied attributes in localized text '
                       f'for {key} with attribute map {attributes}.')
            localized_text = Template(localized_text).safe_substitute(
                attributes)

        logger.debug(f'Final localized text for {key}: {localized_text}')

        return localized_text

    @staticmethod
    def is_valid_language(language: str) -> bool:

        """Returns whether or not a given language code is valid.

        :param language: The language code to check.
        :type language: str

        :return: 'True' if the given language code is supported, 'False'
            otherwise.
        :rtype: bool
        """

        return language in LOCALIZER_SUPPORTED_LANGUAGES

    def switch_language(self, new_language: str) -> None:

        """Changes the language of the localizer.

        :param new_language: The new language to set in the localizer.
        :type new_language: str
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Switching localization language from {self._language} '
                     f'to {new_language}.')

        self._language = new_language
        self._load_language_data()

        logger.debug(f'Localization language was set to {new_language}.')

    def update_localizations(self) -> None:

        """Reloads the localization files to pick up updates."""

        self._data = self._load_language_file(language=self._language)
        if self._cache_default:
            self._default_data = self._load_language_file(
                language=self._default_language)

    def _load_language_from_configuration(self) -> None:

        """Loads the configuration file of the application and retrieves the
        configured language."""

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug('Loading application language from configuration file...')

        filename = os.path.abspath(os.path.expanduser(
            './data/config/launcher.yaml'))

        if not os.path.isfile(filename):
            raise FileNotFoundError(
                f'Configuration file {filename} was not found.')

        content = None
        with open(file=filename, mode='r', encoding='utf-8') as raw:
            file = YAML()
            content = file.load(raw.read())

        self._language = str(content['language']).lower()

        logger.debug(f'Application language has been set as {self._language} '
                     f'in the configuration.')

    def _load_language_file(self, language: str) -> dict:

        """Loads a language file from the virtual file system.

        :param language: The language file to load.
        :type language: str

        :return: The contents of the language file as a dictionary.
        :rtype: dict
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Loading language file for language {language}...')

        filename = os.path.abspath(os.path.expanduser(
            f'{self._localization_directory}/{language}.yaml'))
        if not os.path.isfile(filename):
            logger.error(f'Localization file {filename} was not found.')
            return  {}

        content = None
        with open(file=filename, mode='r', encoding='utf-8') as raw:
            file = YAML()
            content = file.load(raw.read())

        logger.debug(f'Language file for language {language} has been loaded.')

        return content

    def _load_language_data(self) -> None:

        """Loads the language file corresponding to the selected application
        language into memory."""

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Loading language {self._language}...')
        self._data = self._load_language_file(language=self._language)
        logger.debug(f'Language {self._language} has been loaded.')

    def _cache_default_language_data(self) -> None:

        """Loads the default language file into memory to speed up retrieval of
        default language texts when the translation is missing."""

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Loading default language file for language '
                     f'{self._default_language} to memory.')
        self._default_data = self._load_language_file(
            language=self._default_language)
        logger.debug('Default language file loaded to memory.')

    def _load_default_text(self, key: str) -> str:

        """Loads the default version of the given localization key.

        :param key: The localization key to load.
        :type key: str

        :return: The text corresponding to the given localization key from the
            default language file.
        :rtype: str
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Loading default localization text for {key}.')

        if self._cache_default:
            return self._default_language[key]

        data = self._load_language_file(language=self._default_language)

        text = None
        try:
            text = data[key]
        except KeyError:
            logger.error(f'Localization key {key} is not found in the default '
                         f'language file.')
            text = 'KEY NOT FOUND'

        return text

    def _translate_text(self, text: str) -> str:

        """Translates the given text using Google Translate.

        :param text: The text to translate.
        :type text: str

        :return: The translated text.
        :rtype: str
        """

        logger = logging.getLogger(DCSTOOLS_LOG_CHANNEL)
        logger.debug(f'Attempting to translate {text} to {self._language}...')

        translator = Translator()
        try:
            translation = translator.translate(
                text,
                src=self._default_language,
                dest=self._language)
        except httpx.HTTPError as error:
            logger.error(
                f'Failed to translate text {text}. Reason: {error}')
            return text

        logger.debug(f'Received translation for {text}: {translation.text}.')

        return translation.text

LOCALIZER = Localizer()
"""The global localizer instance."""
