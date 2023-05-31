import pandas as pd
import json
import requests
import config.config as config


def return_data(what):
    url_base = "https://api.spotify.com/v1/"

    # Headers for API calls
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer {0}".format(config.api_token),
    }

    # Top Artists/tracks
    api_url = "{0}me/top/{1}".format(url_base, what)
    # print(api_url)

    # Parameters for api calls
    parameters = {"time_range": "long_term", "limit": 20}

    response = requests.get(api_url, headers=headers, params=parameters)
    print(response.status_code)

    # checks for top artists
    if what == "artists":
        data = response.json()
        artist_name = []
        genres = []
        id = []

        # Save all info in lists
        for artist in data["items"]:
            artist_name.append(artist["name"])
            genres.append(artist["genres"])
            id.append(artist["id"])

        # Saving info as dicctionary
        artists_dict = {
            "artist_name": artist_name,
            "genres": genres,
            "id": id,
        }

        spotify_df = pd.DataFrame(artists_dict, columns=["artist_name", "genres", "id"])

    # checks for top tracks
    elif what == "tracks":
        data = response.json()
        track_name = []
        artist_name = []
        album_name = []
        track_id = []
        spotify_url = []

        # Save all info in lists
        for track in data["items"]:
            track_name.append(track["name"])
            artist_name.append(track["artists"][0]["name"])
            album_name.append(track["album"]["name"])
            track_id.append(track["id"])
            spotify_url.append(track["external_urls"]["spotify"])

            # Saving info as dictionary
        track_dict = {
            "track_name": track_name,
            "artist_name": artist_name,
            "album_name": album_name,
            "track_id": track_id,
            "spotify_url": spotify_url,
        }

        spotify_df = pd.DataFrame(
            track_dict,
            columns=[
                "track_name",
                "artist_name",
                "album_name",
                "track_id",
                "spotify_url",
            ],
        )

    else:
        print("Invalid Input")

    return spotify_df
