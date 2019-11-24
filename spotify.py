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
	songs = []

	for i in range(len(words)):
		result = sp.search(words[i])	
		if len(result) > 0:
			song = result['tracks']['items'][0]['name']
			songs.append(song)

	return songs