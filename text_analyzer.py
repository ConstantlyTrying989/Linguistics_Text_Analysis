import re
from collections import Counter
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk
from config.settings import MIN_WORD_LENGTH, PROCESSED_DIR

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class TextAnalyzer:
    """Analyzes linguistic patterns and text statistics"""
    
    def __init__(self):
        print("✓ Text analyzer initialized")
        self.stop_words = set(stopwords.words('english'))
    
    def tokenize_text(self, text):
        """Split text into tokens"""
        tokens = word_tokenize(text.lower())
        return tokens
    
    def get_word_frequency(self, text, top_n=20):
        """Get most common words"""
        tokens = self.tokenize_text(text)
        # Remove stopwords and short words
        filtered = [w for w in tokens if w.isalpha() and len(w) >= MIN_WORD_LENGTH and w not in self.stop_words]
        
        frequency = Counter(filtered)
        return frequency.most_common(top_n)
    
    def get_sentence_count(self, text):
        """Count sentences"""
        sentences = sent_tokenize(text)
        return len(sentences)
    
    def get_word_count(self, text):
        """Count total words"""
        tokens = self.tokenize_text(text)
        words = [w for w in tokens if w.isalpha()]
        return len(words)
    
    def get_unique_words(self, text):
        """Count unique words"""
        tokens = self.tokenize_text(text)
        unique = set([w for w in tokens if w.isalpha()])
        return len(unique)
    
    def analyze_text(self, text):
        """Complete text analysis"""
        analysis = {
            "total_characters": len(text),
            "word_count": self.get_word_count(text),
            "unique_words": self.get_unique_words(text),
            "sentence_count": self.get_sentence_count(text),
            "avg_word_length": len(text) / max(self.get_word_count(text), 1),
            "top_words": self.get_word_frequency(text, top_n=10),
        }
        return analysis
    
    def save_analysis(self, analysis, filename):
        """Save analysis results"""
        try:
            output_path = PROCESSED_DIR / filename
            
            # Prepare data
            top_words_df = pd.DataFrame(analysis['top_words'], columns=['word', 'frequency'])
            top_words_df.to_csv(output_path, index=False)
            
            print(f"✓ Analysis saved to {filename}")
            return True
        except Exception as e:
            print(f"✗ Error saving analysis: {e}")
            return False


def main():
    analyzer = TextAnalyzer()
    
    sample_text = """
    Natural language processing is a fascinating field of artificial intelligence.
    It helps computers understand and work with human language.
    Text analysis reveals patterns, frequencies, and linguistic structures.
    We can extract insights from large volumes of text data.
    """
    
    print("\n📊 Analyzing sample text...")
    results = analyzer.analyze_text(sample_text)
    
    print(f"\nAnalysis Results:")
    print(f"  Characters: {results['total_characters']}")
    print(f"  Words: {results['word_count']}")
    print(f"  Unique Words: {results['unique_words']}")
    print(f"  Sentences: {results['sentence_count']}")
    print(f"  Avg Word Length: {results['avg_word_length']:.2f}")
    print(f"\n  Top 10 Words:")
    for word, freq in results['top_words']:
        print(f"    - {word}: {freq}")
    
    analyzer.save_analysis(results, "analysis_results.csv")


if __name__ == "__main__":
    main()