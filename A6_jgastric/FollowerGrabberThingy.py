from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import time
import json
consumer_key = "lYUHPYN8uCL84oesFXnhH9FSh"
consumer_secret = "wCPmeGp2s5v0mLq3c56aa5PjJMzpV2YxNhy2XAPRuUsMNPrS6X"
access_token = "4856503619-PLk2k6r2pOg33ldUCGOrNaQXJSFVnUk3oRNNweX"
access_token_secret = "SUaYa2LCic9edYkV9fP43R6qKBw03ynKemMQ0bm4G9qOy"




class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	ids = []
	tList2 = {}

	if(api.verify_credentials):
		print("Successfully Logged in")
		print("Getting twitter follower counts list")
		
		v = open('twitter_followers.json','r')
		tList = json.loads(v.readline())
		v.close()

		for key in tList.keys():
			print(key)
			try:
				usr = api.get_user(key)
				tList2[key] = {'twitter_followers_counts': usr.followers_count}
			except:
				print("We got a timeout...sleeping for 15 minutes")
				with open('twitter_followers_counts2.json','w') as f:
					json.dump(tList2,f)
				time.sleep(15*60)
		
		with open('twitter_followers_counts_2.json','w') as f:
			json.dump(tList2,f)