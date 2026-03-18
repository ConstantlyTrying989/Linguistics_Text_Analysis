# Linguistics Text Analysis

Analyze text like a linguist. Extract patterns, word frequencies, and linguistic insights from any text dataset using NLP.

---

## What's the Purpose of this Project

Ever wondered what patterns hide in text? This project automatically analyzes language, pulls out the important words, and shows you what's really being said.

Whether you're researching language patterns, analyzing documents, or exploring NLP - this tool does the heavy lifting for you.

---

## What It Does Right Now

- **Tokenization** - Break text into meaningful pieces
- **Word Frequency Analysis** - Find the most important words
- **Text Statistics** - Character count, word count, unique vocabulary
- **Visualizations** - Charts and word clouds you can actually understand
- **Pattern Detection** - Linguistic insights automatically extracted
- **Export Results** - Save analysis to CSV for further work

---

## Quick Start (2 Minutes)
```bash
# Get the code
git clone https://github.com/ConstantlyTrying989/Linguistics_Text_Analysis.git
cd Linguistics_Text_Analysis

# Set up Python environment
python -m venv venv
venv\Scripts\activate          # Windows
# or
source venv/bin/activate       # Mac/Linux

# Install everything needed
pip install -r requirements.txt

# Run it!
python main.py
```

Done! Your text analyzed in seconds. 🎉

---

## 📊 Current Metrics We Track

**Text Statistics:**
- 📝 Total word count
- 🔤 Unique vocabulary size
- 📄 Sentence count
- 📏 Average word length
- 💾 Character count

**Linguistic Analysis:**
- 🔝 Top 20 most frequent words
- 📈 Word frequency distribution
- 🚫 Stopword filtering
- 🔗 Token-based analysis

**Outputs:**
- CSV format for analysis
- Word frequency rankings
- Statistical breakdowns

---

## What We're Building Next

**Coming Soon:**
- Sentiment analysis (positive/negative/neutral detection)
- Named Entity Recognition (find people, places, organizations)
- Part-of-speech tagging (identify nouns, verbs, adjectives)
- Readability scoring (how easy/hard is the text to read?)
- Text comparison (analyze multiple texts side-by-side)
- Batch processing (analyze multiple files at once)

**Future Ideas:**
- Topic modeling (what's this text really about?)
- Multi-language support (analyze text in other languages)
- Semantic analysis (understand meaning, not just words)
- Chatbot training (use analysis for AI training)
- Trend analysis (how language changes over time)
- Advanced visualizations (interactive dashboards)

**Dream Features:**
- Deep learning NLP models
- Speech-to-text integration
- Academic paper analysis
- Plagiarism detection
- Real-time web scraping and analysis
- Mobile app version

---

## How to Use It

**Analyze text right now:**
```bash
python main.py
```

**Just load text:**
```bash
python scripts/text_loader.py
```

**Just analyze:**
```bash
python scripts/text_analyzer.py
```

**Just visualize:**
```bash
python scripts/visualizer.py
```

---

## Where Everything Lives
```
Linguistics_Text_Analysis/
├── config/           ← Settings and constants
├── scripts/          ← The actual code that does stuff
├── data/
│   ├── datasets/    ← Your text files go here
│   └── processed/   ← Analysis results saved here
├── tests/           ← Tests to make sure it works
├── main.py          ← Run this to do everything
└── requirements.txt ← What Python packages you need
```

---

## Setup Help

**"I got an error about missing `nltk` or `config`"**
```bash
pip install -r requirements.txt
pip install nltk
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

**"Config module not found"**
- Make sure you're in the project root folder
- Terminal should show: `(venv) C:\...\ Linguistics_Text_Analysis>`
- Run: `python scripts/text_analyzer.py` (NOT from inside scripts folder)

**"Virtual environment won't activate"**
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`
- Should see `(venv)` at start of terminal

**"Can't see charts appearing"**
- Make sure you have matplotlib: `pip install matplotlib`
- Make sure wordcloud is installed: `pip install wordcloud`

---

## Want to Help?

Got ideas? Found a bug? Want to add features?

1. Fork the project on GitHub
2. Make your changes
3. Submit a pull request
4. That's it!

Some ideas:
- Add sentiment analysis
- Create better visualisations
- Support more languages
- Write tutorials
- Suggest new features

---

## The Boring Stuff

**License:** MIT (you can use this however you want, even commercially)

**Built With:** Python, NLTK, Pandas, Matplotlib, WordCloud

---

## Want to Support This?

If you find this useful, give it a ⭐ on GitHub! It helps others find it and keeps me motivated to add cool features.
```
https://github.com/ConstantlyTrying989/Linguistics_Text_Analysis
```
