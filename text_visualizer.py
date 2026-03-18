import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from config.settings import PROCESSED_DIR

class TextVisualizer:
    """Creates visualizations from text analysis"""
    
    def __init__(self):
        print("✓ Visualizer initialized")
        plt.style.use("seaborn-v0_8-darkgrid")
    
    def plot_word_frequency(self, words_freq, title="Word Frequency"):
        """Plot top words"""
        try:
            words, frequencies = zip(*words_freq)
            
            plt.figure(figsize=(12, 6))
            plt.barh(words, frequencies)
            plt.xlabel("Frequency")
            plt.title(title)
            plt.tight_layout()
            plt.show()
            print("✓ Word frequency chart created")
        except Exception as e:
            print(f"✗ Error creating chart: {e}")
    
    def create_wordcloud(self, text):
        """Create word cloud"""
        try:
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
            
            plt.figure(figsize=(12, 6))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.tight_layout()
            plt.show()
            print("✓ Word cloud created")
        except Exception as e:
            print(f"✗ Error creating word cloud: {e}")
    
    def plot_text_statistics(self, stats_dict):
        """Plot text statistics"""
        try:
            metrics = ['word_count', 'unique_words', 'sentence_count']
            values = [stats_dict.get(m, 0) for m in metrics]
            
            plt.figure(figsize=(10, 6))
            plt.bar(metrics, values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
            plt.ylabel("Count")
            plt.title("Text Statistics")
            plt.tight_layout()
            plt.show()
            print("✓ Statistics chart created")
        except Exception as e:
            print(f"✗ Error creating statistics chart: {e}")


def main():
    viz = TextVisualizer()
    
    # Example data
    word_freq = [('language', 15), ('text', 12), ('analysis', 10), ('data', 8), ('processing', 7)]
    viz.plot_word_frequency(word_freq)


if __name__ == "__main__":
    main()