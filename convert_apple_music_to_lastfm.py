import csv
import datetime
import json

output_json = []
with open("play_history.csv", newline='', encoding="utf-8") as csv_file:
        history_file = csv.reader(csv_file)
        skip = False
        for row in history_file:
              skip = not skip
              if skip:
                    continue
              
              artist_and_track = row[0].split('-')
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
              