"""MTGJSON Version 4 Initializer"""
import logging
import pathlib
import time
from typing import Dict, List

# Maintenance variables
__VERSION__ = "4.1.0"
__VERSION_DATE__ = "2018-11-11"
__MAINTAINER__ = "Zach Halpern (GitHub: @ZeldaZach)"
__MAINTAINER_EMAIL__ = "zahalpern+github@gmail.com"
__REPO_URL__ = "https://github.com/mtgjson/mtgjson4"

# Globals
SUPERTYPES: List[str] = ["Basic", "Host", "Legendary", "Ongoing", "Snow", "World"]
BASIC_LANDS: List[str] = ["Plains", "Island", "Swamp", "Mountain", "Forest"]
TOP_LEVEL_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
COMPILED_OUTPUT_DIR: pathlib.Path = TOP_LEVEL_DIR.joinpath("set_outputs")
LOG_DIR: pathlib.Path = TOP_LEVEL_DIR.joinpath("logs")
CONFIG_PATH: pathlib.Path = TOP_LEVEL_DIR.joinpath("mtgjson.properties")
RESOURCE_PATH: pathlib.Path = TOP_LEVEL_DIR.joinpath("mtgjson4").joinpath("resources")

# Compiled Output Files
ALL_SETS_OUTPUT: str = "AllSets"
ALL_CARDS_OUTPUT: str = "AllCards"
SET_CODES_OUTPUT: str = "SetCodes"
SET_LIST_OUTPUT: str = "SetList"
KEY_WORDS_OUTPUT: str = "Keywords"

LANGUAGE_MAP: Dict[str, str] = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese (Brazil)",
    "ja": "Japanese",
    "ko": "Korean",
    "ru": "Russian",
    "zhs": "Chinese Simplified",
    "zht": "Chinese Traditional",
    "he": "Hebrew",
    "la": "Latin",
    "grc": "Ancient Greek",
    "ar": "Arabic",
    "sa": "Sanskrit",
    "px": "Phyrexian",
}

# Logging configuration
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(
            str(
                LOG_DIR.joinpath(
                    "mtgjson_" + str(time.strftime("%Y-%m-%d_%H:%M:%S")) + ".log"
                )
            )
        ),
    ],
)
