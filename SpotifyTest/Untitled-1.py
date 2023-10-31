import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
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
        print(track_id)
        break

#print(spotify.audio_features(track_id))

data = spotify.audio_analysis(track_id)

for i in data['track']:
    if i == 'codestring':
        break
    print(i,data['track'][i])

for i in data['sections']:
    print(i)
