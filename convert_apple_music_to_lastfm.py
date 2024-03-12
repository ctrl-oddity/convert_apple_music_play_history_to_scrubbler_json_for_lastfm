import csv
import datetime
import json

output = []
output_json = []
with open("play_history.csv", newline='', encoding="utf-8") as csv_file:
        #history_file = csv.reader(csv_file, delimiter=',', quotechar='|')
        history_file = csv.reader(csv_file)
        skip = False
        for row in history_file:
              skip = not skip
              if skip:
                    continue
              
              #print(row)
              artist_and_track = row[0].split('-')
              artist = artist_and_track[0].strip()
              track = artist_and_track[1].strip()
              timestamp_value = int(row[1]) 
              datetime_value = datetime.datetime.fromtimestamp(timestamp_value / 1000)
              #print(datetime_value.strftime("%d/%m/%y %H:%M"))
              #print(f"{track} : \"{artist}\" [{datetime_value}]")
              datetime_value = datetime_value.strftime("%m/%d/%Y %H:%M")
              line = f"\"{artist}\", \"\", \"{track}\", {datetime_value}, \"\", 00:03:00"
              print(line)
              output.append(line)
              output_json.append([artist, track, datetime_value])
              #data = [artist, track, datetime_value]
              #output.append(data)

with open("lastfm_history.csv", 'w', newline='') as csv_file:
       csv_file.write('\n'.join(output))

with open("lastfm_history.json", 'w') as json_file:
    #csv_file.write('\n'.join(output))
    json_data = []
    for row in output_json:
        #print(row)
        dictionary = {
            "artistName": row[0],
            "trackName": row[1],
            "ts": row[2],
        }
        #json_object = json.dumps(dictionary, indent=4)
        ##json_file.write(json_object)
        #json_data.append(json_object)
        json_data.append(dictionary)

    #json_content = json.dumps({json_data}, indent=4)
    #json_file.write(json_content)
    json.dump(json_data, json_file)
              