import sys
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pprint
import json

with open(os.path.join("config", "keys.json")) as read_file:
	data = json.load(read_file)
# Dev IDs
os.environ['SPOTIPY_CLIENT_ID'] = data['client_id']
os.environ['SPOTIPY_CLIENT_SECRET'] = data['client_secret']
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://www.google.com'

# Set up connection to API
client_credentials_manager = SpotifyClientCredentials()
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(
str(sys.argv[1]), scope, client_id=os.environ['SPOTIPY_CLIENT_ID'], client_secret=os.environ['SPOTIPY_CLIENT_SECRET'], redirect_uri='http://www.google.com')
sp = spotipy.Spotify(auth=token)


# Search for an artist and adds the first five songs to a predefined playlist
def show_tracks(results):
	for i, item in enumerate(results['items']):
		track = item['track']
		print(track)

if len(sys.argv) > 2:
	username = str(sys.argv[1])
	response = sp.featured_playlists()
	print(response['message'])
	playlists = sp.user_playlists(username)
	for playlist in playlists['items']:
		print()
		print(playlist['name'])
		results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
		pprint.pprint(results[0]['tracks'])
		# show_tracks(tracks)
		# while tracks['next']:
		#	tracks = sp.next(tracks)
		#	show_tracks(tracks)
#	search_str = sys.argv[2]
#	playlist_name = sys.argv[3]
#
#	result = sp.search(search_str)
#	i = 1
#
#	playlists = sp.user_playlist_create(username, playlist_name)
#	while i < 6:
#		track = json.dumps(result["tracks"]['items'][i]['id'])
#		i += 1
#		sp.user_playlist_add_tracks(username, playlists['id'], [track.replace('"','')])
#else:
 #   print("Can't find artist.")
