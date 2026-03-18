import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from text_loader import TextLoader
from text_analyzer import TextAnalyzer
from text_visualizer import TextVisualizer

def main():
    print("\n" + "="*50)
    print("LINGUISTICS TEXT ANALYSIS PIPELINE")
    print("="*50 + "\n")
    
    # Step 1: Load
    print("[1/3] TEXT LOADING PHASE")
    loader = TextLoader()
    sample_text = "Natural language processing analyzes text patterns. " * 5
    loader.texts.append(sample_text)
    
    # Step 2: Analyze
    print("\n[2/3] TEXT ANALYSIS PHASE")
    analyzer = TextAnalyzer()
    analysis = analyzer.analyze_text(sample_text)
    
    print(f"\nAnalysis Results:")
    print(f"  Total Words: {analysis['word_count']}")
    print(f"  Unique Words: {analysis['unique_words']}")
    print(f"  Sentences: {analysis['sentence_count']}")
    print(f"  Average Word Length: {analysis['avg_word_length']:.2f}")
    print(f"\nTop 5 Words:")
    for word, freq in analysis['top_words'][:5]:
        print(f"  - {word}: {freq}")
    
    analyzer.save_analysis(analysis, "text_analysis.csv")
    
    # Step 3: Visualize
    print("\n[3/3] VISUALIZATION PHASE")
    viz = TextVisualizer()
    viz.plot_word_frequency(analysis['top_words'], "Most Common Words")
    
    print("\n" + "="*50)
    print("✓ PIPELINE COMPLETED SUCCESSFULLY")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()