import os

def add_songs(*args):

    songs = {}

    for data in args:
        if data[0] not in songs:
            songs[data[0]] = []
        songs[data[0]].extend(data[1])

    result = []
    for song,lyric in songs.items():
        result.append(f"- {song}")
        if lyric:
            result.extend(lyric)

    return os.linesep.join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
