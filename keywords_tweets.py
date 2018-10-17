# Import the necessary methods from tweepy library
import tweepy
from tweepy import OAuthHandler


# Variables that contains the user credentials to access Twitter API
consumer_key = 'GwpuXi1ZMyc0ATSb3FEPaTyOU'
consumer_secret = '0Y1jaPrDOa0uGsxQc4DSDphRWPPYCtVZ0TtvgZorAvzywIZtXJ'
access_token_key = '220846580-ZUElx1lLAd5XRxrL9hYVG6CBkbjLUl3ftvCGIMqE'
access_token_secret = 'WEFkSeH59z92ptB76tGKnh8l6mMKmWN1fVKqV6dYCuc77'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

# The search term you want to find
# query = ['Anxiety','depression','Bipolar', 'schizophrenia','disorder', 'PTSD', 'ADHD', 'Attention Deficit Hyperactivity Disorder']
query = ["I have been diagnosed with Anxiety", 'I have been diagnosed with depression','Anxiety','depression','Bipolar', 'schizophrenia','disorder', 'PTSD', 'ADHD', 'Attention Deficit Hyperactivity Disorder']
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
for a in query:
    print("+++++now searching for " + a)
    results = api.search(q = a, lang=language)

    # foreach through all tweets pulled
    for tweet in results:
        # printing the text stored inside the tweet object
        if tweet.place:
            print(tweet.user.screen_name, "Tweeted:", tweet.text)
        # print(tweet.user.screen_name)



