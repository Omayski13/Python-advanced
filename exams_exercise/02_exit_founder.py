players = input().split(", ")
p1, p2 = players[0],players[1]
matrix = [[x for x in input().split()] for _ in range(6)]
turns = 0

p1_hit = 0
p2_hit = 0
command = input()
while True:
    data_row,data_col = command.split(", ")
    row = int(data_row[1])
    col = int(data_col[0])
    if turns % 2 == 0:
        if p1_hit > 0:
            turns += 1
            p1_hit = 0
            command = input()
            continue
    elif turns % 2 != 0:
        if p2_hit > 0:
            turns += 1
            p2_hit = 0
            command = input()
            continue

    if matrix[row][col] == "T":
        if turns % 2 == 0:
            print(f"{p1} is out of the game! The winner is {p2}.")
        elif turns % 2 != 0:
            print(f"{p2} is out of the game! The winner is {p1}.")
            turns +=1
        break
    if matrix[row][col] == "E":
        if turns % 2 == 0:
            print(f"{p1} found the Exit and wins the game!")
        elif turns % 2 != 0:
            print(f"{p2} found the Exit and wins the game!")
            turns +=1
        break
    if matrix[row][col] == "W":
        if turns % 2 == 0:
            print(f"{p1} hits a wall and needs to rest.")
            p1_hit += 1
        elif turns % 2 != 0:
            print(f"{p2} hits a wall and needs to rest.")
            p2_hit += 1

    command = input()
    turns += 1