import tweepy
#import simplejson
from tweepy import OAuthHandler
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="8bMfTL9OBefuh9NGfEQsA"
consumer_secret="nfuIKC0BMchSC3PTDFKOCCC0ZiejPcliwL7hP3FW8o"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="1535863993-wd8ha1pikBBzgIHveH3KQ08Fo54uxLPUdNw3LMx"
access_token_secret="hKOb7zKf7WhS1Enfxy0bEEQJv9sTIS2LFkcXkhi7Q"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print api.me().name

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's 
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps

#api.update_status('Updating using OAuth authentication via Tweepy!')
