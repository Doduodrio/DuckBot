import datetime
import discord

X = ':regional_indicator_x:' # or whatever the code is for discord emojis
O = ':o2:'
blank = ':black_large_square:'
player, bot = X, O
deepest = 99 # max recursions

def make_move(board, symbol, move):
  # returns the new board state after making a move
  # board is the current board state
  # symbol is the symbol to be placed
  # move is index of the target space
  return [*board[0:move], symbol, *board[move::]]

def win(b):
    # returns winner if there is one, else returns None
    # b is the current board state because i don't want to type board[] a billion times
    if blank not in b:
        return
    win_states = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
        (0, 4, 8), (2, 4, 6) # diagonals
    ]
    for i in win_states:
        if b[i[0]]!=0 and b[i[0]]==b[i[1]] and b[i[1]]==b[i[2]]:
            return list[i[0]]
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
    if depth == 99 or (winner is not None):
        if winner == player:
            return 10 - depth
        elif winner == bot:
            return depth - 10
        else:
            return 0
    
    available = [i for i in range(9) if new_board[i] == 0]
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
    def __init__(self):
        self.board = [0 for i in range(9)]
        self.winner = None

    def get_embed(self):
        embed = discord.Embed(
            color = discord.Color.dark_teal(),
            title = 'Tic Tac Toe',
            description = '',
            timestamp = datetime.datetime.now()
        )
        for i in range(9):
            self.description += self.board[i]
            if i%3==2:
                self.description += '\n'
        if self.winner:
            embed.add_field(name='', value=f'{self.winner} was the winner!')

        return embed

    async def send(self, message: discord.Message): # player starts by default, but add option to pick starting player later
        self.message = await message.channel.send(embed=self.get_embed(), view=self)

    @discord.ui.button(style=discord.ButtonStyle.primary, row=0)
    async def a1(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        b.disabled = True
        await self.update(0)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, row=0)
    async def a2(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        b.disabled = True
        await self.update(1)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, row=0)
    async def a3(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        b.disabled = True
        await self.update(2)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, row=1)
    async def b1(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        b.disabled = True
        await self.update(3)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, row=1)
    async def b2(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        b.disabled = True
        await self.update(4)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, row=1)
    async def b3(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        b.disabled = True
        await self.update(5)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, row=2)
    async def c1(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        b.disabled = True
        await self.update(6)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, row=2)
    async def c2(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        b.disabled = True
        await self.update(7)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, row=2)
    async def c3(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        b.disabled = True
        await self.update(8)
    
    async def update(self, player_choice):
        await self.message.edit(embed=self.get_embed(), view=self)