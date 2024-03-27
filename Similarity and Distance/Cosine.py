import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

twitter = """
Twitter is an online social media and social networking service owned and operated by American company X Corp.,
the legal successor of Twitter, Inc. Twitter users outside the United States are legally served by the Ireland-based
Twitter International Unlimited Company, which makes these users subject to Irish and European Union data protection laws.
On Twitter users post texts, photos and videos known as 'tweets'. Registered users can tweet, like, 'retweet' tweets,
and direct message (DM) other registered users, while unregistered users only have the ability to view public tweets.
Users interact with Twitter through browser or mobile frontend software, or programmatically via its APIs.
"""
facebook = """
Facebook is an online social media and social networking service owned by American technology giant Meta Platforms.
Created in 2004 by Mark Zuckerberg with fellow Harvard College students and roommates Eduardo Saverin, Andrew McCollum,
Dustin Moskovitz, and Chris Hughes, its name derives from the face book directories often given to American university students.
Membership was initially limited to only Harvard students, gradually expanding to other North American universities and,
since 2006, anyone over 13 years old. As of December 2022, Facebook claimed 2.96 billion monthly active users, and ranked third
worldwide among the most visited websites. It was the most downloaded mobile app of the 2010s. Facebook can be accessed from devices
with Internet connectivity, such as personal computers, tablets and smartphones. After registering, users can create a profile
revealing information about themselves. They can post text, photos and multimedia which are shared with any other users who have
agreed to be their friend' or, with different privacy settings, publicly. Users can also communicate directly with each other with
Messenger, join common-interest groups, and receive notifications on the activities of their Facebook friends and the pages they follow.
"""

# Convert the texts into TF-IDF vectors
docs = [twitter, facebook]
vectorizer = CountVectorizer()
vect1 = vectorizer.fit_transform(docs)
print(vect1)
print(vectorizer.get_feature_names_out())

# Calculate the cosine similarity between the vectors
similarity = cosine_similarity(vect1)
print(similarity)