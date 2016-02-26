from twitter import *

config = {}
consumer_key = "lYUHPYN8uCL84oesFXnhH9FSh"
consumer_secret = "wCPmeGp2s5v0mLq3c56aa5PjJMzpV2YxNhy2XAPRuUsMNPrS6X"
access_token = "4856503619-PLk2k6r2pOg33ldUCGOrNaQXJSFVnUk3oRNNweX"
access_token_secret = "SUaYa2LCic9edYkV9fP43R6qKBw03ynKemMQ0bm4G9qOy"
twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
source = "ideoforms"
target = "lewisrichard"
result = twitter.friendships.show(source_screen_name = source,
                                  target_screen_name = target)
following = result["relationship"]["target"]["following"]
follows   = result["relationship"]["target"]["followed_by"]
print "%s following %s: %s" % (source, target, follows)
print "%s following %s: %s" % (target, source, following)