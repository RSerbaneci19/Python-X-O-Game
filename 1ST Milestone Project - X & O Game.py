
# coding: utf-8
THE X & O GAME - 1ST MILESTONE
# In[16]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print('-------------')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    print('-------------')


# In[17]:


def player_input():
    player_marker_1 = ''
    player_marker_2 = ''
    while player_marker_1 != 'X' and player_marker_1 != 'O':
        player_marker_1 = input('Player 1, please choose X or O : ').upper()
    
    if player_marker_1 == 'X':
        player_marker_2 = 'O'
    else:
        player_marker_2 = 'X'
        
    print('Player 1 has choosen {p1}, therefore Player 2 is going to be playing with {p2}. Good Luck !'.format(p1 = player_marker_1, p2 = player_marker_2))
    return (player_marker_1, player_marker_2)


# In[18]:


def place_marker(board, marker, position):
    board[position] = marker


# In[19]:


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or #Horizontal Check
    (board[4] == board[5] == board[6] == mark) or #Horizontal Check
    (board[1] == board[2] == board[3] == mark) or #Horizontal Check
    (board[7] == board[4] == board[1] == mark) or #Vertical Check
    (board[8] == board[5] == board[2] == mark) or #Vertical Check
    (board[9] == board[6] == board[3] == mark) or #Vertical Check
    (board[7] == board[5] == board[3] == mark) or #Diagonal Check
    (board[9] == board[5] == board[1] == mark)) #Diagonal Check


# In[20]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[21]:


def space_check(board, position):
    return board[position] == ' '


# In[22]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[23]:


def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[24]:


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[ ]:


# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to X and O')

while True:
    
    # PLAY THE GAME
    ## SET EVERYTHING UP ( BOARD, WHO IS FIRST, CHOOSE MARKERS)
    the_board = [' '] * 10
    player_marker_1, player_marker_2 = player_input()
    
    who_is_first = choose_first()
    print(who_is_first + ' will start first')
    
    ready_for_game = input('Are you ready to play ? Please reply with Yes or No: ')
    if ready_for_game.lower().startswith('y'):
        game_on = True
    else:
        game_on = False
    
    ## GAME PLAY
    while game_on:
        
        if who_is_first == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player_marker_1, position)
            
            if win_check(the_board, player_marker_1):
                display_board(the_board)
                print('Player 1 has WON !!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a TIE')
                    game_on = False
                else:
                    who_is_first = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player_marker_2, position)
            
            if win_check(the_board, player_marker_2):
                display_board(the_board)
                print('Player 2 has WON !!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a TIE')
                    game_on = False
                else:
                    who_is_first = 'Player 1'

    if not replay():
        break


# ## Good Job!
