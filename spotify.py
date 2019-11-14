from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import sys
import os
import pprint
import json

with open(os.path.join("config", "keys.json")) as read_file:
	data = json.load(read_file)
# Dev IDs
os.environ['SPOTIPY_CLIENT_ID'] = data['client_id']
os.environ['SPOTIPY_CLIENT_SECRET'] = data['client_secret']
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://www.google.com'

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def addWords(words = []):
	i = 0
	songs = []
	while(i < len(words)):
		for w in words:
			result = sp.search(w)	
			song = result['tracks']['items'][i]['name']
			songs.append(song)
		i += 1

	return songs