import datetime
import discord

X = ':regional_indicator_x:' # or whatever the code is for emojis
O = ':o2:'
blank = ':black_large_square:'
player, bot = 1, 2
deepest = 99 # max recursions

def move_piece(board, player, move):
  # returns the new board state after making a move
  # board is the current board state
  # player is either "X" or "O"
  # move is index of the target space
  return [*board[0:move], player, *board[move::]]

def win(b):
    # returns winner if there is one, else returns None
    # b is the current board state
    if 0 not in b:
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
    # a is the symbol of the current player (1 or 2)
    # b is the symbol of the other player (1 or 2)
    # target is the spot where the symbol will be placed
    # depth is the number of recursions
    # maximizing is if we are the maximizing player or not

    new_board = move_piece(board, a, target)

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
        if self.winner:
            embed.add_field(name='', value=f'{self.winner} is the winner!')

        return embed

    async def send(self, message: discord.Message):
        self.message = await message.channel.send(embed=self.get_embed(), view=self)

    @discord.ui.button(style=discord.ButtonStyle.primary, label='<', row=0)
    async def a1(self, i: discord.Interaction, b: discord.ui.Button):
        await i.response.defer()
        await self.update()
    
    async def update(self):
        await self.message.edit(embed=self.get_embed(), view=self)