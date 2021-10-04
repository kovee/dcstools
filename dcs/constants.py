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

"""Contains common constants used throughout the codebase."""

DCSTOOLS_LOG_CHANNEL = 'dcstools'
"""Log channel to use for writing logs."""

DCS_STEAM_PATH = 'c:/Program Files (x86)/Steam/steamapps/common/DSCWorld'
"""The typical install directory of DCS when installed from Steam."""

DCS_ED_PATH = 'c:/Program Files/Eagle Dynamics/DCS World'
"""The default installation path offered by the DCS World installer downloaded
from the Eagle Dynamics website."""

DCS_WORKING_DIRECTORY = '~/Saved Games/DCS'
"""Path to the DCS working directory."""

TARGET_PATH = 'c:/Program Files (x86)/Thrustmaster/TARGET'
"""The default installation directory of T.A.R.G.E.T."""

TARGET_EXECUTABLE = 'x64/TARGETGUI.exe'
"""Path to the T.A.R.G.E.T. executable inside the installation path."""

PSVR_INSTALL_DIRECTORY = 'c:/Program Files (x86)/TrinusPSVR'
"""Path to the directory where Trinus PSVR is installed by default."""

PSMOVESERVICE_INSTALL_DIRECTORY = 'c:/Program Files/PSMoveService'
"""Path to the directory where PSMoveService is installed by default."""

PSMOVESERVICE_EXECUTABLE = 'bin/PSMoveService.exe'
"""Path to the PSMoveService executable inside the installation directory."""

FREEPIE_INSTALL_DIRECTORY = 'c:/Program Files (x86)/FreePIE'
"""Path to the directory where FreePIE is installed by default."""

FREEPIE_EXECUTABLE = 'FreePIE.exe'
"""Name of the FreePIE executable file."""

LOCALIZER_SUPPORTED_LANGUAGES = \
[
    'af',   # Afrikaans
    'sq',   # Albanian
    'am',   # Amharic
    'ar',   # Arabic
    'hy',   # Armenian
    'az',   # Azerbaijani
    'eu',   # Basque
    'be',   # Belarusian
    'bn',   # Bengali
    'bs',   # Bosnian
    'bg',   # Bulgarian
    'ca',   # Catalan
    'ceb',  # Cebuano
    'zh',   # Chinese (Simplified)
    'zh-TW',# Chinese (Traditional)
    'co',   # Corsican
    'hr',   # Croatian
    'cs',   # Czech
    'da',   # Danish
    'nl',   # Dutch
    'en',   # English
    'eo',   # Esperanto
    'et',   # Estonian
    'fi',   # Finnish
    'fr',   # French
    'fy',   # Frisian
    'gl',   # Galician
    'ka',   # Georgian
    'de',   # German
    'el',   # Greek
    'gu',   # Gujarati
    'ht',   # Haitian Creole
    'ha',   # Hausa
    'haw',  # Hawaiian (ISO-639-2)
    'he',   # Hebrew
    'iw',   # Hebrew
    'hi',   # Hindi
    'hmn',  # Hmong (ISO-639-2)
    'hu',   # Hungarian
    'is',   # Icelandic
    'ig',   # Igbo
    'id',   # Indonesian
    'ga',   # Irish
    'it',   # Italian
    'ja',   # Japanese
    'jv',   # Javanese
    'kn',   # Kannada
    'kk',   # Kazakh
    'km',   # Khmer
    'rw',   # Kinyarwanda
    'ko',   # Korean
    'ku',   # Kurdish
    'ky',   # Kyrgyz
    'lo',   # Lao
    'la',   # Latin
    'lv',   # Latvian
    'lt',   # Lithuanian
    'lb',   # Luxembourgish
    'mk',   # Macedonian
    'mg',   # Malagasy
    'ms',   # Malay
    'ml',   # Malayalam
    'mt',   # Maltese
    'mi',   # Maori
    'mr',   # Marathi
    'mn',   # Mongolian
    'my',   # Myanmar (Burmese)
    'ne',   # Nepali
    'no',   # Norwegian
    'ny',   # Nyanja (Chichewa)
    'or',   # Odia (Oriya)
    'ps',   # Pashto
    'fa',   # Persian
    'pl',   # Polish
    'pt',   # Portuguese (Portugal, Brazil)
    'pa',   # Punjabi
    'ro',   # Romanian
    'ru',   # Russian
    'sm',   # Samoan
    'gd',   # Scots Gaelic
    'sr',   # Serbian
    'st',   # Sesotho
    'sn',   # Shona
    'sd',   # Sindhi
    'si',   # Sinhala (Sinhalese)
    'sk',   # Slovak
    'sl',   # Slovenian
    'so',   # Somali
    'es',   # Spanish
    'su',   # Sundanese
    'sw',   # Swahili
    'sv',   # Swedish
    'tl',   # Tagalog (Filipino)
    'tg',   # Tajik
    'ta',   # Tamil
    'tt',   # Tatar
    'te',   # Telugu
    'th',   # Thai
    'tr',   # Turkish
    'tk',   # Turkmen
    'uk',   # Ukrainian
    'ur',   # Urdu
    'ug',   # Uyghur
    'uz',   # Uzbek
    'vi',   # Vietnamese
    'cy',   # Welsh
    'xh',   # Xhosa
    'yi',   # Yiddish
    'yo',   # Yoruba
    'zu'    # Zulu
]
"""
List of supported languages as specified by Google at
https://cloud.google.com/translate/docs/languages.
"""

DEFAULT_LOCALE = 'en'
"""The default language of the application."""

DEFAULT_LOCALIZATION_PATH = './data/locale'
"""Path to the directory where language files are stored."""

DEFAULT_PROFILES_PATH = './data/profiles'
"""Path to the directory containing the user profiles."""

DEFAULT_PLANES_PATH = './data/planes'
"""Path to the directory containing the plane configurations."""
