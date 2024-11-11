import datetime
import discord
import time

class GoFirst(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.player_starts = None
    
    def get_embed(self):
        return discord.Embed(
            color = discord.Color.dark_teal(),
            title = 'Tic Tac Toe',
            description = 'Do you want to go first?',
            timestamp = datetime.datetime.now()
        )

    async def send(self, message: discord.Message):
        return await message.channel.send(embed=self.get_embed(), view=self)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='Yes')
    async def yes(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        self.player_starts = True
        self.stop()
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='No')
    async def no(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        self.player_starts = False
        self.stop()


# actual game code below

X = ':regional_indicator_x:' # note to future self: or whatever the code is for discord emojis
O = ':o2:'
blank = ':black_large_square:'
player, bot = X, O
deepest = 99 # max recursions

def make_move(board, symbol, move):
  # returns the new board state after making a move
  # board is the current board state
  # symbol is the symbol to be placed
  # move is index of the target space
  return [*board[0:move], symbol, *board[move+1::]]

def win(b):
    # returns winner if there is one, else returns None
    # b is the current board state because i don't want to type board[] a billion times
    win_states = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
        (0, 4, 8), (2, 4, 6) # diagonals
    ]
    for i in win_states:
        if b[i[0]] != blank:
            if b[i[0]]==b[i[1]] and b[i[1]]==b[i[2]]:
                return b[i[0]]
    if blank not in b:
        return 'tie'
    return

def minimax(board, a, b, target, depth, maximizing):
    # returns the value of the selected branch of the game tree
    # board is the current board state
    # a is the symbol of the current player
    # b is the symbol of the other player
    # target is the spot where the symbol will be placed
    # depth is the number of recursions
    # maximizing is if we are the maximizing player or not

    new_board = make_move(board, a, target)

    winner = win(new_board)
    if depth == deepest or (winner is not None):
        if winner == player:
            return 10 - depth # 10 pts with depth penalty (maximizing player)
        elif winner == bot:
            return -10 + depth # -10 pts with depth bonus (minimizing bot)
        else:
            return 0
    
    available = [i for i in range(9) if new_board[i]==blank]
    if maximizing:
        value = -999
        for position in available:
            value = max(value, minimax(new_board, b, a, position, depth+1, not maximizing))
        return value
    else:
        value = 999
        for position in available:
            value = min(value, minimax(new_board, b, a, position, depth+1, not maximizing))
        return value

class TicTacToe(discord.ui.View):
    def __init__(self, player_starts):
        super().__init__()
        self.board = [blank for i in range(9)]
        self.player_starts = player_starts
        self.player = X
        self.bot = O
        self.winner = None

    def get_embed(self, text=''):
        embed = discord.Embed(
            color = discord.Color.dark_teal(),
            title = 'Tic Tac Toe',
            description = '',
            timestamp = datetime.datetime.now()
        )
        for i in range(9):
            embed.description += self.board[i]
            if i%3==2:
                embed.description += '\n'
        if self.winner == 'tie':
            embed.add_field(name='', value='It was a tie!')
        elif self.winner:
            embed.add_field(name='', value=f'{self.winner} was the winner!')
        else:
            embed.add_field(name='', value=text)

        return embed
    
    async def update(self, text):
        print('    ' + 'Updating board...')
        await self.message.edit(embed=self.get_embed(text), view=self)

    async def make_board(self, message: discord.Message):
        if self.player_starts:
            self.message = await message.edit(embed=self.get_embed("Player's turn"), view=self)
        else:
            self.message = await message.edit(embed=self.get_embed('Bot is thinking...'), view=self)
            await self.bot_move()

    @discord.ui.button(style=discord.ButtonStyle.primary, label='A1', row=0)
    async def a1(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.player_move(0)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='A2', row=0)
    async def a2(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.player_move(1)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='A3', row=0)
    async def a3(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.player_move(2)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='B1', row=1)
    async def b1(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.player_move(3)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='B2', row=1)
    async def b2(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.player_move(4)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='B3', row=1)
    async def b3(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.player_move(5)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='C1', row=2)
    async def c1(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.player_move(6)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='C2', row=2)
    async def c2(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.player_move(7)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label='C3', row=2)
    async def c3(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.player_move(8)
    
    def disable_button(self, index):
        # disables the specified button
        for i in range(len(self.children)):
            if i==index:
                self.children[i].disabled = True
                print('        ' + f'Disabled button {i}')
                return
    
    async def game_end(self):
        # displays winner and ends interaction
        await self.message.edit(embed=self.get_embed(), view=self)
        print('    ' + f'The winner was {self.winner}!')
        for i in range(9):
            self.disable_button(i)
        self.stop()
    
    async def player_move(self, player_choice):
        available = [i for i in range(9) if self.board[i]==blank]

        # update board with player's move
        if player_choice in available:
            self.board = make_move(self.board, self.player, player_choice)
            print('        ' + f'Player placed piece on {player_choice}')
            self.disable_button(player_choice)
        else:
            await self.update('Spot already taken. Please pick again.') # should be impossible, but just in case
            print('        ' + f'Player could not place piece on {player_choice} because it was already taken')

        # check if player won
        if win(self.board) is None:
            await self.update('DuckBot is thinking...')
            print('    ' + "It is now DuckBot's turn")
            await self.bot_move()
        else:
            self.winner = win(self.board)
            print('        ' + 'End of game detected, so calling game_end()')
            await self.game_end()
    
    async def bot_move(self):
        time.sleep(1)
        
        available = [i for i in range(9) if self.board[i]==blank]

        # generate and update board with bot's move
        if self.board == [blank for i in range(9)]:
            bot_choice = 4
        else:
            scores = [minimax(self.board, self.bot, self.player, i, 0, True) for i in available]
            bot_choice = available[scores.index(min(scores))] # pick branch that results in min score for player
            print('        ' + f'Scores: {[(available[i], scores[i]) for i in range(len(available))]}')
        self.board = make_move(self.board, self.bot, bot_choice)
        print('        ' + f'DuckBot placed piece on {bot_choice}')
        self.disable_button(bot_choice)

        # check if bot won
        if win(self.board) is None:
            await self.update("Player's turn")
            print('    ' + "It is now Player's turn")
        else:
            self.winner = win(self.board)
            print('        ' + 'End of game detected, so calling game_end()')
            await self.game_end()