import csv
import datetime
import json

# formatting an apple music track play history file gotten via https://privacy.apple.com/
# to a json format supported by the app Last.fm-Scrubbler-WPF-Beta-1.28

output_json = []
with open("Apple Music - Track Play History.csv", newline='', encoding="utf-8") as csv_file:
        history_file = csv.reader(csv_file)
        skip = True
        prev = []
        for row in history_file:
              if skip:
                 skip = False
                 continue
              
              artist_and_track = row[0].split(" - ")
              if len(artist_and_track) < 2:
                continue

              # try to fix the duplication issue (true vs. false)
              # this will of course make repeated listening of a song wrong
              # but that shouldn't be too common
              if artist_and_track == prev:
                continue
              
              prev = artist_and_track

              artist = artist_and_track[0].strip()
              track = artist_and_track[1].strip()
              timestamp_value = int(row[1]) 
              datetime_value = datetime.datetime.fromtimestamp(timestamp_value / 1000)
              datetime_value = datetime_value.strftime("%m/%d/%Y %H:%M")
              output_json.append([artist, track, datetime_value])

with open("lastfm_history.json", 'w') as json_file:
    json_data = []
    for row in output_json:
        dictionary = {
            "artistName": row[0],
            "trackName": row[1],
            "ts": row[2],
        }
        json_data.append(dictionary)

    json.dump(json_data, json_file)
              