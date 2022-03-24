import tweepy
import time

consumer_key = 'xxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxx'

key = 'xxxxxxxxxxxxxxxxxxxx'
secret = 'xxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

FILE_NAME = 'lastseen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    global last_seen_id
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen():
    file_write = open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

search = '#ikokazike'
sch = search
nrTweets = 2000

tweets = tweepy.Cursor(api.search, sch).items(nrTweets)

for tweet in tweets:
    try:
        tweet.retweet()
        print('Tweet Retweeted')
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
