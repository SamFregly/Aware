#Import the necessary methods from tweepy library
import ssl
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token ="3648600621-Qr0HWRdUZ4GP7bwk6nzbIFmdriflsgNcqR22gS8"
access_token_secret ="5C9QBwYz8HSw3EhjarMVl0oj4TooAbugkgrjNA4MSCYWc"
consumer_key ="Pz9OLoKLvyr496hZOfS0S5p0l"
consumer_secret ="Vx29mWbIACRRqeTPuBSNAvDA9poWUFy37MnfurpZ19nsCqvvlJ"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['bernie', 'sanders', 'hillary', 'clinton' , 'trump','jeb', 'bush', 'democrat', 'republican', 'president', 'bernie2016'])
