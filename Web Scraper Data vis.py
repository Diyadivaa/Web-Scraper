import csv
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

# Read the quotes from the CSV file
quotes = []
with open('quotes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)
    for row in reader:
        quotes.append(row[0])

# Create a word cloud from the quotes
wordcloud = WordCloud().generate(' '.join(quotes))

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Read the quotes from the CSV file
quotes = []
with open('quotes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)
    for row in reader:
        quotes.append(row[0])

# Split the quotes into words
words = []
for quote in quotes:
    words += quote.split()

# Count the occurrences of each word
word_counts = Counter(words)

# Get the top 10 most popular words
top_words = word_counts.most_common(10)

# Extract the words and counts into separate lists
words, counts = zip(*top_words)

# Create a bar chart
plt.bar(words, counts)
plt.xticks(rotation=45)
plt.show()


# Read the quotes and authors from the CSV file
quotes = []
authors = []
with open('quotes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        quotes.append(row[0])
        authors.append(row[1])

# Count the occurrences of each author
author_counts = Counter(authors)

# Get the top 10 most used authors
top_authors = author_counts.most_common(10)

# Extract the authors and counts
authors, counts = zip(*top_authors)

# Plot the author counts as a bar chart
plt.bar(authors, counts)
plt.show()