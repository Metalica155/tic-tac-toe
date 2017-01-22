import os

print "Welcome to the tic tac toe mothaaaa fakka!\n"

board = []
board_value = []
players = {}
active_player = "player1"


clear = lambda: os.system('clear')


def init_board():
    '''
    This will initialize the global game board Dictionary.
    Also initialize the active_player disctionary
    No parameters.
    No return statement.
    '''
    global board
    global board_value
    global players


    board_value = [[0,0,0],[0,0,0],[0,0,0]]
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    players = {'player1': {'name': 'Player 1', 'icon': 'X', 'value': 1},
                    'player2': {'name': 'Player 2', 'icon': 'O', 'value': -1}}

def set_player(player_id, player_name):
    '''
    Set the player Name and used icon
    INPUT: A player id 'player1', a string name and a charackter
    '''
    global players

    players[player_id]['name'] = player_name

def player_input():
    '''
    This will take the player input and change the game board.
    '''
    global players
    output_string = players[active_player]['name'] + ":"

    while True:
        input = raw_input(output_string)
        if check_input(input):
            player_step = transform_input(input)
            if steper(player_step):
                break


def change_active_player():
    global active_player

    if active_player == 'player1':
        active_player = 'player2'
    else:
        active_player = 'player1'

def steper(step):
    '''
    Make a step.
    OUTPUT: True or False depending on if the step is valid
    '''
    global board_value

    if board_value[step[0]][step[1]] == 0:
        board_value[step[0]][step[1]] = players[active_player]['value']
    else:
        return False

    return True

def check_input(input):
    '''
    Check the input if its valid.
    '''
    input_list = list(input)

    if input_list[0] == 'a' or input_list[0] == 'b' or input_list[0] == 'c':
        if input_list[1] == '1' or input_list[1] == '2' or input_list[1] == '3':
            return True

    return False

def transform_input(input):

    input_list = list(input)

    for index, item in enumerate(input_list):
        if item == 'a' or item == '1':
            input_list[index] = 0
        elif item == 'b' or item == '2':
            input_list[index] = 1
        elif item == 'c' or item == '3':
            input_list[index] = 2

    return input_list

def draw_board():
    '''
    This will draw the game board to the screen.
    '''
    clear()
    index = 0
    abc = ['a','b','c']
    print "\n 1  2  3  "
    for row in board:
        print "{index}|{a}|{b}|{c}|".format(a = row[0], b = row[1], c = row[2],
                index = abc[index])
        index += 1

    print "\n"

def synch_boards():
    global board
    check = lambda char: ' ' if char == 0 else 'X' if char == 1 else '0'

    #board = []
    #board = board_value

    for i in range( len( board ) ):
        for y in range(3):
            board[i][y] = check(board_value[i][y])

def check_win():
    '''
    Checks if some of the player won.
    Return with True or False
    '''

    #use absolute value  cuz |3| and |-3| is the same
    for row in board_value:
        if row[0] + row[1] + row[2] == 3 or row[0] + row[1] + row[2] == -3:
            return True

    if board_value[0][0] + board_value[1][1] + board_value[2][2] == 3:
        return True

    if board_value[0][0] + board_value[1][1] + board_value[2][2] == -3:
        return True

    if board_value[0][2] + board_value[1][1] + board_value[2][0] == 3:
        return True

    if board_value[0][2] + board_value[1][1] + board_value[2][0] == -3:
        return True

    return False
def get_players():

    player1_name = check_init_player('First Player name:')
    player2_name = check_init_player('Secound Player name:')


    set_player('player1',player1_name)
    set_player('player2',player2_name)

    #global active_player
    #active_player = players['player1']['name']

def check_init_player(input_string):

    while True:
        temp = raw_input(input_string)
        if type(temp) == type('na ez egy string'):
            return temp


def game():
    clear()
    init_board()
    get_players()
    round = 0
    while True:
        round += 1
        clear()
        synch_boards()
        draw_board()
        if round > 9:
            print "\n\t\tDontetlen!"
            break
        player_input()
        if check_win():
            synch_boards()
            draw_board()
            print  "\n\t\t{player} nyert!".format(player=players[active_player]['name'])
            break
        change_active_player()


while True:
    game()
    q = raw_input('Akartok meg jatszani? y/n ')
    if q == 'n':
        break
    if q == 'y':
        pass
