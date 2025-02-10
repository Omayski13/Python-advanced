matrix = [[x for x in input().split()]for _ in range(6)]
points = 0


turns = 0
while turns < 3:
    data = input().strip("()")
    data = data.split(", ")
    hit_row = int(data[0])
    if not 0 <= hit_row < 6:
        turns += 1
        continue
    hit_col = int(data[1])
    if not 0 <= hit_col < 6:
        turns += 1
        continue
    if matrix[hit_row][hit_col] == "H":
        turns += 1
        continue
    if matrix[hit_row][hit_col] == "B":
        for index in range (6):
            if matrix[index][hit_col] == "B":
                continue
            points += int(matrix[index][hit_col])
        matrix[hit_row][hit_col] = "H"

    turns += 1

if points >= 100:
    if 100 <= points < 200:
        print(f"Good job! You scored {points} points, and you've won Football.")
    elif 200 <= points < 300:
        print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
    if points >= 300 :
        print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")

