import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'client_id'
client_secret = 'client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Obtenim les cançons de cada playlist
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

# Agafem la informació que ens interessa
def extract_track_info(track):
    track_info = {
        'id':track['track']['id'],
        'title': track['track']['name'],
        'artist': track['track']['artists'][0]['name'],
        'album': track['track']['album']['name'],
        'release_date': track['track']['album']['release_date'],
        'duration_ms': track['track']['duration_ms'],
        'spotify_url': track['track']['external_urls']['spotify']
    }
    return track_info

# Creem la llista de palylists que volem analitzar, ja que no volem totes les del compte
playlist_ids = ['3zb78wIWvn9X1so8dceWca', '3LVAF8rnqurv9Kzdo8kAsT', '1WacouuToRBMhBlVUVbnzT', '3vsvh15C5NYUXLjBazAVh3', '4vuUpAwE3vTIWf3CTou0wB', '1P0z4BsLOwtrpGEm7wPqFA', '5vcielrvT47NdtHF9VrG9z', '7rT0e4vvH7hHJnFLULVN8m', '6eppRY4vIjAlTCfmtXT4Vy', '0Tx3fUnxs0ZE0O7A8DQozJ']

# Iterem per a cada playlist
for playlist_id in playlist_ids:
    tracks = get_playlist_tracks(playlist_id)
    playlist_data = []
    for track in tracks:
        track_info = extract_track_info(track)
        playlist_data.append(track_info)

    # Desem les dades en un JSON
    playlist_name = sp.playlist(playlist_id)['name']
    filename = f'{playlist_name}.json'
    with open(f'datasets/songs-playlists/{filename}', 'w') as json_file:
        json.dump(playlist_data, json_file, indent=4)

    print(f"Playlist '{playlist_name}' data saved to {filename}.")
