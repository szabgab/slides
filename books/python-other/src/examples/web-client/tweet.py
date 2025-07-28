import configparser
import twitter
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'api.cfg'));
api = twitter.Api( **config['twitter'] )

status = api.PostUpdate('My first Tweet using Python')
print(status.text)

