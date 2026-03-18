import pandas as pd
from pathlib import Path
from config.settings import DATASETS_DIR

class TextLoader:
    """Loads text data from various sources"""
    
    def __init__(self):
        print("✓ Text loader initialized")
        self.texts = []
        self.metadata = {}
    
    def load_txt_file(self, filename):
        """Load a single text file"""
        try:
            filepath = DATASETS_DIR / filename
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            self.texts.append(text)
            print(f"✓ Loaded {filename} ({len(text)} characters)")
            return text
        except Exception as e:
            print(f"✗ Error loading {filename}: {e}")
            return None
    
    def load_csv_text(self, filename, text_column):
        """Load text from CSV file"""
        try:
            filepath = DATASETS_DIR / filename
            df = pd.read_csv(filepath)
            texts = df[text_column].tolist()
            self.texts.extend(texts)
            print(f"✓ Loaded {len(texts)} texts from {filename}")
            return df
        except Exception as e:
            print(f"✗ Error loading CSV: {e}")
            return None
    
    def get_all_texts(self):
        """Get all loaded texts"""
        return self.texts


def main():
    loader = TextLoader()
    # Example: load sample text
    sample_text = "Natural language processing is fascinating. Text analysis helps us understand language patterns."
    loader.texts.append(sample_text)
    print(f"\n✓ Loaded sample text with {len(sample_text)} characters")


if __name__ == "__main__":
    main()