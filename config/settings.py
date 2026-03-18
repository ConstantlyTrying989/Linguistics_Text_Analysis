import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATASETS_DIR = DATA_DIR / "datasets"
PROCESSED_DIR = DATA_DIR / "processed"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories
DATASETS_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Analysis settings
DEBUG_MODE = True
LOG_LEVEL = "INFO"
MIN_WORD_LENGTH = 3
STOP_WORDS_LANGUAGE = "english"

# NLP settings
TOKENIZER_TYPE = "nltk"  # Options: nltk, spacy
ANALYSIS_TYPES = ["frequency", "sentiment", "pos_tagging", "readability"]

# Output settings
OUTPUT_FORMAT = "csv"  # Options: csv, json, both
VISUALIZATION_ENABLED = True