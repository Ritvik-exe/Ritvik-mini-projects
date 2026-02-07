import random

# Initializing global score variables to track points across multiple rounds
player_score = 0
bot_score = 0

# List of valid moves for the game and for the bot to choose from
choose = ['rock', 'paper', 'scissor']

# Game Logic Map: The 'Key' is the move, and the 'Value' is what that move beats.
# This replaces complex nested if/else statements.
rules = { 'rock' : 'scissor',
         'paper' : 'rock',
         'scissor' : 'paper'
}

def victory(player, bot):
    """ Determines the winner of a single round and updates global scores. """
    global player_score
    global bot_score

    if rules[player] == bot: # Check if the player's choice beats the bot's choice
        print('Player win!')
        player_score += 1

    elif bot == player:
        print('Draw')

    else:
        print('Bot win!')
        bot_score += 1

# Main Game Loop  
print('---------------------Play Rock, Paper, Scissor!---------------------')

while True:
    # 1. Handle User Input
    player_move = input('Enter rock, paper or scissor (press 0 to stop game): ').lower()

    # 2. Check for Exit Condition
    if player_move == '0':
        print('-----------------------------Game finshed-----------------------------')
        print(f'Player points: {player_score}')
        print(f'Bot points: {bot_score}')
         # Determine the overall match winner
        if player_score > bot_score:
            print('Player won!')
        if bot_score > player_score:
            print('Bot won!')
        else:
            print('Draw')
            break
    
    # 3. Validate Input: Check if the move exists in our 'choose' list
    if player_move not in choose:
        print('Invalid input!')
        continue

    # 4. Generate Bot Move
    bot_move = random.choice(choose)
    print(f'bot choice: {bot_move}')

    # 5. Determine Winner
    victory(player_move, bot_move)
