import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from PIL import Image
import numpy as np
import random
#pip install spotipy --upgrade
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="c0c6529a1097408fbe4ccd7a804a4604", client_secret="555973a776d047589c9f4556c0e29009"))

track = "Dance Monkey"
artist = "Tones And I"
artist = artist.lower()
track_id = ""

searchQuery = track + ' ' + artist
searchResults = spotify.search(q=searchQuery)

#only print the song id
for i in searchResults['tracks']['items']:
    if i['artists'][0]['name'].lower() == artist and i['name'] == track:
        track_id = i['id']
        break

#print(spotify.audio_features(track_id))

data = spotify.audio_analysis(track_id)

for i in data['track']:
    if i == 'codestring':
        break

array = []
for i in data['sections']:
    array.append([(i['start'],i['duration'],i['tempo']),(i['time_signature']*i['duration'],i['tempo']*i['tempo_confidence'],i['start'])])
        
array = np.array(array, dtype=np.uint8)
img = Image.fromarray(array)
img.save('output.png')