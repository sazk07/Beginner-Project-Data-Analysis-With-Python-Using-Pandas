"""
twitter sentiment analysis
"""
tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]

happy_words=['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words=['sad', 'bad', 'tragic', 'unhappy', 'worst']

COUNT_HAPPY_TWEETS=int()
COUNT_SAD_TWEETS=int()

for tweet in tweets:
    for word in happy_words:
        if word in tweet:
            COUNT_HAPPY_TWEETS = COUNT_HAPPY_TWEETS + 1
    for word in sad_words:
        if word in tweet:
            COUNT_SAD_TWEETS = COUNT_SAD_TWEETS + 1
print(f"Number of happy tweets: {COUNT_HAPPY_TWEETS}")
HAPPY_FRACTION = COUNT_HAPPY_TWEETS/len(tweets)
print(f"The fraction of happy tweets is: {HAPPY_FRACTION}")
print(f"Number of sad tweets: {COUNT_SAD_TWEETS}")
SAD_FRACTION = COUNT_SAD_TWEETS/len(tweets)
print(f"The fraction of sad tweets is: {SAD_FRACTION}")
SENTIMENT_SCORE = COUNT_HAPPY_TWEETS - COUNT_SAD_TWEETS
print(f"The sentiment score for the given tweets is {SENTIMENT_SCORE}")
if SENTIMENT_SCORE > 0:
    print("The overall sentiment is happy")
else:
    print("The overall sentiment is sad")
