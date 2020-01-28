GRID_SIZE = 5


def draw_line(width, edge, filling):
    print(filling.join([edge] * (width + 1)))


def display_winner(player):
    if player == 0:
        print("Tie")
    else:
        print("Player " + str(player) + " wins!")

def check_row_winner(row):
    """
    Return the player number that wins for that row.
    If there is no winner, return 0.
    """
    if row[0] == row[1] and row[1] == row[2]:
        return row[0]
    return 0

def get_col(game, col_number):
    return [game[x][col_number] for x in range(GRID_SIZE)]

def get_row(game, row_number):
    return game[row_number]

def check_winner(game):
    game_slices = []
    maxed = GRID_SIZE-1
    for index in range(GRID_SIZE):
        game_slices.append(get_row(game, index))
        game_slices.append(get_col(game, index))

    # check diagonals
    down_diagonal = [game[x][x] for x in range(GRID_SIZE)]
    up_diagonal = [game[x][maxed-x] for x in range(GRID_SIZE)]
    game_slices.append(down_diagonal)
    game_slices.append(up_diagonal)

    for game_slice in game_slices:
        winner = check_row_winner(game_slice)
        if winner != 0:
            return winner

    return winner

def start_game():
    row = [0 for x in range(GRID_SIZE)]
    return [row for x in range(GRID_SIZE)]

def display_game(game):
    d = {2: "O", 1: "X", 0: "_"}
    draw_line(GRID_SIZE, " ", "_")
    for row_num in range(GRID_SIZE):
        new_row = []
        for col_num in range(GRID_SIZE):
            new_row.append(d[game[row_num][col_num]])
        print("|" + "|".join(new_row) + "|")


def add_piece(game, player, row, column):
    """
    game: game state
    player: player number
    row: 0-index row
    column: 0-index column
    """
    game[row][column] = player
    return game

def check_space_empty(game, row, column):
    return game[row][column] == 0

def convert_input_to_coordinate(user_input):
    try:
        return int(user_input) - 1
    except Exception:
        pass

def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1

def moves_exist(game):
    for row_num in range(GRID_SIZE):
        for col_num in range(GRID_SIZE):
            if game[row_num][col_num]:
                return True
    return False

if __name__ == '__main__':
    game = start_game()
    display_game(game)
    player = 1
    winner = 0  # the winner is not yet defined

    # go on forever
    while winner == 0:
        if moves_exist(game):
            continue
        print("Currently player: " + str(player))
        available = False
        while not available:
            row = convert_input_to_coordinate(input("Which row? (start with 1) "))
            column = convert_input_to_coordinate(input("Which column? (start with 1) "))
            available = check_space_empty(game, row, column)
        game = add_piece(game, player, row, column)
        display_game(game)
        player = switch_player(player)
        winner = check_winner(game)
    display_winner(winner)
