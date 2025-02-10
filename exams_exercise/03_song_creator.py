import os

def add_songs(*args):
    songs = {}
    result = []
    for song,lyric in args:
        if song not in songs:
            if type(lyric) == list:
                songs[song] = lyric
            else:
                songs[song] = [lyric]
        else:
            if type(lyric) == list:
                songs[song].append(lyric)
            else:
                songs[song] = [lyric]

    for song,lyric in songs.items():
        result.append(f"- {song}\n")
        for lyrics in lyric:
            if not lyrics:
                continue
            if type(lyrics) == list:
                result.append(f"{', '.join(lyrics)}\n")
            else:
                result.append(f"{lyrics}\n")
    return os.linesep.join(result)




print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
