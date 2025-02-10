def team_lineup(*args):
    football_dict = {}
    result = []




    for data in args:
        footballer = data[0]
        nationality = data[1]
        if nationality not in football_dict:
            football_dict[nationality] = []
        football_dict[nationality].append(footballer)

        sorted_dict = dict(sorted(football_dict.items(),key=lambda x: (-len(x[1]), x[0])))

    for nationality,players in sorted_dict.items():
        result.append(f"{nationality}:\n")
        for player in players:
            result.append(f"  -{player}\n")
    return "".join(result)






# print(team_lineup(
#     ("Harry Kane", "England"),
#     ("Manuel Neuer", "Germany"),
#     ("Raheem Sterling", "England"),
#     ("Toni Kroos", "Germany"),
#     ("Cristiano Ronaldo", "Portugal"),
#     ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))


# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany"),
#    ("Bruno Fernandes", "Portugal"),
#    ("Bernardo Silva", "Portugal"),
#    ("Harry Maguire", "England")))

