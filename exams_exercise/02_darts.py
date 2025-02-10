names = input().split(", ")
n1 = names[0]
n2 = names[1]
my_dict = {n1: [0, 501], n2: [0,501]}

matrix = [[x for x in input().split()]for _ in range(7)]

special_symbols = ["D","T","B"]
turn = 0
player = ''
while True:
    data = input().strip("()")
    command = data.split(", ")
    current_row = int(command[0])
    current_col = int(command[1])
    turn += 1
    if turn % 2 == 0:
        player = n2
        my_dict[player][0] += 1
    else:
        player = n1
        my_dict[player][0] += 1
    if not 0 <= current_row < 7 or not 0 <= current_col < 7:
        continue
    if matrix[current_row][current_col] in special_symbols:
        if matrix[current_row][current_col] == "B":
            print(f"{player} won the game with {my_dict[player][0]} throws!")
            break
        else:
            upper_row = int(matrix[0][current_col])
            down_row = int(matrix[6][current_col])
            left_col = int(matrix[current_row][0])
            right_col = int(matrix[current_row][6])
            all_sum = upper_row + down_row + left_col + right_col
            if matrix[current_row][current_col] == "D":
                my_dict[player][1] -= all_sum * 2
                if my_dict[player][1] <= 0:
                    print(f"{player} won the game with {my_dict[player][0]} throws!")
                    break
            if matrix[current_row][current_col] == "T":
                my_dict[player][1] -= all_sum * 3
                if my_dict[player][1] <= 0:
                    print(f"{player} won the game with {my_dict[player][0]} throws!")
                    break
    else:
        my_dict[player][1] -= int(matrix[current_row][current_col])
        if my_dict[player][1] <= 0:
            print(f"{player} won the game with {my_dict[player][0]} throws!")
            break






