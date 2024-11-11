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

class MyView(discord.ui.View):
    def __init__(self):
        self.left_button = discord.ui.Button(
            style = discord.ButtonStyle.primary,
            label = '<'
        )
        self.right_button = discord.ui.Button(
            style = discord.ButtonStyle.primary,
            label = '>'
        )

    async def send(self, message: discord.Message):
        self.message = await message.channel.send(embed=get_embed(), view=self)
    
    async def update(self):
        await self.message.edit(embed=get_embed(), view=self)

    async def left_button_press(self):
        page -= 1
        if page == 0:
            self.left_button.disabled = True # why must i use self.left_button and not just left_button defined in the class body?
        await self.update()
    
    async def right_button_press(self): # note to future self: figure out how to attach these functions to the button objects
        page += 1
        if page == len(data)-1:
            self.right_button.disabled = True
        await self.update()