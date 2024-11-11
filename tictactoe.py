import datetime
import discord

data = range(1, 11)
page = 0

def get_embed():
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = 'This is a test',
        description = f'The number is {data[page]}',
        timestamp = datetime.datetime.now()
    )
    embed.add_field(name='', value=f'Page {page} of {len(data)}')

    return embed

class TicTacToe(discord.ui.View):
    async def send(self, message: discord.Message):
        self.message = await message.channel.send(embed=get_embed(), view=self)

    @discord.ui.button(style = discord.ButtonStyle.primary, label = '<')
    async def left_button(self, i: discord.Interaction, b: discord.ui.Button):
        page -= 1
        if page == 0:
            b.disabled = True # why must i use self.left_button and not just left_button defined in the class body?
        await self.update()
    
    @discord.ui.button(style = discord.ButtonStyle.primary, label = '>')
    async def right_button(self, i: discord.Interaction, b: discord.ui.Button): # note to future self: figure out how to attach these functions to the button objects
        page += 1
        if page == len(data)-1:
            b.disabled = True
        await self.update()
    
    async def update(self):
        if page == 0:
            self.left_button.disabled = True
            self.right_button.disabled = False
        elif page == len(data)-1:
            self.left_button.disabled = False
            self.right_button.disabled = True
        else:
            self.left_button.disabled = False
            self.right_button.disabled = False
        await self.message.edit(embed=get_embed(), view=self)