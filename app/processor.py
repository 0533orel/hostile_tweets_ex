import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


try:
    nltk.data.find("sentiment/vader_lexicon")
except LookupError:
    nltk.download("vader_lexicon")

class Processor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.analyzer = SentimentIntensityAnalyzer()

    def add_rare_word(self):
        rare_words = []
        for text in self.df["original_text"]:
            words = text.split()
            if not words:
                rare_words.append("")
                continue

            word_count = {}
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            rare_word = None
            rare_count = None
            for word, count in word_count.items():
                if rare_count is None or count < rare_count:
                    rare_word = word
                    rare_count = count

            rare_words.append(rare_word)

        self.df["rarest_word"] = rare_words

    def add_sentiment(self):
        sentiments = []
        for text in self.df["original_text"]:
            score = self.analyzer.polarity_scores(text)["compound"]
            if score >= 0.5:
                sentiments.append("positive")
            elif score <= -0.5:
                sentiments.append("negative")
            else:
                sentiments.append("neutral")

        self.df["sentiment"] = sentiments

    def add_weapon(self, blacklist):
        found = []
        for text in self.df["original_text"]:
            text_lower = text.lower()
            weapon = ""
            for w in blacklist:
                if w.lower() in text_lower:
                    weapon = w
                    break
            found.append(weapon)

        self.df["weapons_detected"] = found

    def process(self, blacklist):
        self.add_rare_word()
        self.add_sentiment()
        self.add_weapon(blacklist)
        return self.df


