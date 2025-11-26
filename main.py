import os
import spotipy
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
