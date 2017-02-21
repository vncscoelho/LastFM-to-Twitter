# -*- coding: utf-8 -*-
import json
import requests
import tweepy


def getArtists(apiKey, user):
    weekly_artists = requests.get(
        "http://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user=" + user + "&api_key=" + apiKey + "&format=json")
    return json.loads(weekly_artists.content)


def getTracks(apiKey, user):
    weekly_tracks = requests.get(
        "http://ws.audioscrobbler.com/2.0/?method=user.getweeklytrackchart&user=" + user + "&api_key=" + apiKey + "&format=json")
    return json.loads(weekly_tracks.content)


def getTwitterAPI(apiKey):
    auth = tweepy.OAuthHandler(
        apiKey['consumer_key'], apiKey['consumer_secret'])
    auth.set_access_token(apiKey['access_token'],
                          apiKey['access_token_secret'])
    return tweepy.API(auth)


def tweet(api, message):
	print(repr(message), message)
	return api.update_status(status=message)


def main():
	# Put here API keys:
	lastFM_user = ""  # Your Last.fm user
    lastFM_apiKey = "" # Last.fm API key    
    twitter_apiKeys = { # Twitter API keys
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_token_secret": ""
    }
    auth = getTwitterAPI(twitter_apiKeys)
    artists = getArtists(lastFM_apiKey, lastFM_user)
    track = getTracks(lastFM_apiKey, lastFM_user)

    # Custom message
    message = "Top 3 artists of the week " + "➖".decode('utf-8') + " " + artists["weeklyartistchart"]["artist"][0]["name"] + " (" + artists["weeklyartistchart"]["artist"][0]["playcount"] + "), " + artists["weeklyartistchart"]["artist"][1]["name"] + " (" + artists["weeklyartistchart"][
        "artist"][1]["playcount"] + "), " + artists["weeklyartistchart"]["artist"][2]["name"] + " (" + artists["weeklyartistchart"]["artist"][2]["playcount"] + ")" + "\nMost played: " + "➖".decode('utf-8') + " " + track["weeklytrackchart"]["track"][0]["name"] + " - " + track["weeklytrackchart"]["track"][0]["artist"]["#text"] + " #lastfm"

    tweet(auth, message)

if __name__ == "__main__":
    main()
