import pandas as pd
import json
import requests
import config
from datetime import datetime
import datetime


def return_data():
    url_base = "https://api.spotify.com/v1/"

    # Headers for API calls
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer {0}".format(config.api_token),
    }

    # Getting dates
    today = datetime.datetime.now()
    # last weeks's date
    week = today - datetime.timedelta(days=7)
    week_unix_time = int(week.timestamp()) * 1000

    # Parameters for api calls
    parameters = {"limit": 50, "after": week_unix_time}

    # Recently Played

    api_url = "{0}me/player/recently-played".format(url_base)

    response = requests.get(api_url, headers=headers, params=parameters)

    data = response.json()
    song_names = []
    artist_name = []
    played_at = []

    # Save all info in lists
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_name.append(song["track"]["album"]["artists"][0]["name"])
        played_at.append(song["played_at"])

    # Saving info as dicctionary
    song_dict = {
        "song_name": song_names,
        "artist_name": artist_name,
        "played_at": played_at,
    }

    spotify_df = pd.DataFrame(
        song_dict, columns=["song_name", "artist_name", "played_at"]
    )

    return spotify_df
