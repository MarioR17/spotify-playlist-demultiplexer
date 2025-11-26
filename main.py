import os
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=(
        "playlist-modify-public "
        "playlist-modify-private "
        "user-library-read"
    )
))

user = sp.current_user()

if user:
    print(f"Authenticated as: {user['display_name']} (ID: {user['id']})")
else:
    print("Could not retrieve user details")

print("\n--- Fetching Playlists ---")
playlists = sp.current_user_playlists(limit=5)

if playlists:
    if not playlists['items']:
        print("No playlists found.")
    else:
        first_playlist = playlists['items'][0]
        print(f"Testing with Playlist: '{first_playlist['name']}' (ID: {first_playlist['id']})")

        results = sp.playlist_items(first_playlist['id'], limit=1)
        
        if results:
            if len(results['items']) > 0:
                item = results['items'][0]
                track = item['track']

                print("\n--- Validated Song Data ---")
                print(f"Name:   {track['name']}")
                print(f"Artist: {track['artists'][0]['name']}")
                print(f"URI:    {track['uri']}")
                
            else:
                print("The first playlist was empty!")
