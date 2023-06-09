import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'client_id'
client_secret = 'client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Obtenim audio features
def get_song_features(song_id):
    features = sp.audio_features(song_id)[0]
    return features

# Treiem la llista de fitxers
folder_path = 'datasets/songs-playlists'
json_files = [file for file in os.listdir(folder_path) if file.endswith('.json')]

# Processem cada JSON
for json_file in json_files:
    json_path = os.path.join(folder_path, json_file)

    with open(json_path, 'r') as file:
        data = json.load(file)

    song_data_list = []
    for song in data:
        song_id = song['id']
        song_info = {
            'title': song['title'],
            'artist': song['artist'],
            'album': song['album'],
            'release_date': song['release_date'],
            'duration_ms': song['duration_ms'],
            'spotify_url': song['spotify_url']
        }
        song_features = get_song_features(song_id)

        # Juntem les dades
        song_data = {**song_info, **song_features}
        song_data_list.append(song_data)

    # Desem les dades en un JSON
    output_file = os.path.splitext(json_file)[0] + '_data.json'
    output_path = os.path.join('datasets/song-info', output_file)
    with open(output_path, 'w') as output:
        json.dump(song_data_list, output, indent=4)

    print(f"Song data saved to {output_file}.")
